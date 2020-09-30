import math
import bisect


class Path:
    def __init__(self, position: dict, target: dict, past_distance: int = 0, path_list: [] = None, changes=0,
                 vector_orientation=None):
        self.changes = changes
        self.vector_orientation = vector_orientation
        if path_list is None:
            self.path_list = [position]
            self.past_distance = 0
        else:
            self.path_list = path_list
            self.past_distance = past_distance + position["distance"]
            next_orientation = [position["i"] - self.path_list[-1]["i"], position["j"] - self.path_list[-1]["j"]]
            self.path_list.append(position)
            if self.vector_orientation is not None:
                if self.vector_orientation != next_orientation:
                    self.changes += 1
            self.vector_orientation = next_orientation
        self.target = target
        # if len(self.path_list) > 2:
        #     self.changes = 0
        #     position = self.path_list[1]
        #     old_orientation = [position["i"] - self.path_list[0]["i"], position["j"] - self.path_list[0]["j"]]
        #     old_position = position
        #     for position_index in range(2,len(self.path_list)):
        #         position = self.path_list[position_index]
        #         orientation = [position["i"] - old_position["i"], position["j"] - old_position["j"]]
        #         if orientation != old_orientation:
        #             self.changes += 1
        #         old_orientation = orientation
        #         old_position = position
        self.best_distance = self.past_distance + math.sqrt(
            (position["i"] - target["i"]) ** 2 + (position["j"] - target["j"]) ** 2)

    def copy_add(self, position):
        path_list = self.path_list.copy()
        return Path(position, self.target, self.past_distance, path_list, self.changes, self.vector_orientation)

    def __float__(self):
        return self.best_distance - 1 / (1 + self.changes) + 1

    def __gt__(self, other):
        return float(self) > float(other)

    def __ge__(self, other):
        return float(self) >= float(other)

    def __lt__(self, other):
        return float(self) < float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    def __contains__(self, item):
        for position in self.path_list:
            if position["i"] == item["i"] and position["j"] == item["j"]:
                return True
        return False


class SortedPaths:
    def __init__(self, path: Path):
        self.list = [path]

    def pop(self, index: int):
        return self.list.pop(index)

    def add(self, path: Path):
        bisect.insort(self.list, path)
