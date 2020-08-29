import math


class Path:
    def __init__(self, position: dict, target: dict, past_distance: int = 0, path_list: [] = None):
        if path_list is None:
            self.path_list = [position]
            self.past_distance = 0
        else:
            self.path_list = path_list
            self.past_distance = past_distance + position["distance"]
            self.path_list.append(position)
        self.target = target
        self.best_distance = self.past_distance + math.sqrt(
            (position["i"] - target["i"]) ** 2 + (position["j"] - target["j"]) ** 2)

    def copy_add(self, position):
        path_list = self.path_list.copy()
        return Path(position, self.target, self.past_distance, path_list)

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

    def add(self, path: Path, i0: int = 0, i1: int = -1):
        if i1 == -1:
            i1 = len(self.list) - 1
            if i1 == -1:
                self.list.append(path)
                return
        median = int((i1 + i0) * 0.5)
        if path.best_distance <= self.list[median].best_distance:
            if median == i0:
                return self.list.insert(median, path)
            self.add(path, i0, median)
        else:
            if median == i0:
                if path.best_distance <= self.list[i1].best_distance:
                    self.list.insert(i1, path)
                    return
                else:
                    self.list.insert(i1 + 1, path)
                    return
            self.add(path, median, i1)
