import math
from itertools import permutations

from structure.Node import Node
from structure.Path import Path, SortedPaths

diagonal = math.sqrt(2)
non_diagonal = 1


def print_matrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


def distance_prediction(position, past_distance, target):
    future_distance = math.sqrt((position["i"] - target["i"]) ** 2 - (position["j"] - target["j"]) ** 2)
    return past_distance + future_distance


def basic_positions(size: int):
    positions = [0] * (2 * size + 1)
    value = 1
    for i in range(0, size):
        positions[size - (i + 1)] = value
        positions[size + i + 1] = -value
        value += 1
    return positions


def is_possible(list_values: list, position_index: int):
    return len(list_values) > position_index >= 0 and \
           (position_index == 0 or isinstance(list_values[position_index - 1], int)) and \
           isinstance(list_values[position_index], int) and \
           (position_index + 1 == len(list_values) or isinstance(list_values[position_index + 1], int))


class Graph:
    def __init__(self):
        self.nodes = {}
        self.map = None

    def add_dict_node(self, name: str, data, children: []):
        node = Node(name, data, children)
        self.add_node(node)

    def add_node(self, node: Node):
        self.nodes[node.name] = node

    def set_parents(self):
        for node_name in self.nodes:
            for child in self.nodes[node_name].children:
                self.nodes[child].parents.add(node_name)

    def get_edges_size(self, node_name):
        node = self.nodes[node_name]
        distance = 0
        for parent_name in node.parents:
            parent_node = self.nodes[parent_name]
            distance += math.sqrt((node.position["i"] - parent_node.position["i"]) ** 2 + (
                    node.position["j"] - parent_node.position["j"]) ** 2)
        for child_name in node.children:
            child_node = self.nodes[child_name]
            distance += math.sqrt((node.position["i"] - child_node.position["i"]) ** 2 + (
                    node.position["j"] - child_node.position["j"]) ** 2)
        return distance/(len(node.parents) + len(node.children)) if distance != 0 else 0

    def create_matrix(self):
        layers = self.find_layer_orientation()
        largest_layer_size = 0
        for layer in layers:
            if len(layer) > largest_layer_size:
                largest_layer_size = len(layer)
        if largest_layer_size % 2 == 0:
            largest_layer_size = largest_layer_size + 1
        width = largest_layer_size * 2 + 1
        median = int(width * 0.5)
        matrix = [[0] * width]
        min_matrix = []
        for layer_index in range(len(layers)):
            layer = layers[layer_index]
            row = [0] * width
            layer_size = len(layer)
            if layer_size % 2 == 0:
                layer_size = layer_size + 1
            i = median - (layer_size - 1)
            positions = []
            for node_name in layer:
                row[i] = node_name
                self.nodes[node_name].set_position(layer_index * 2 + 1, i)
                positions.append((layer_index * 2 + 1, i))
                i = i + 2
                if i == median and len(layer) % 2 == 0:
                    i = i + 2
            matrix.append(row)
            min_matrix.append(positions)
            matrix.append([0] * width)

        for i in range(10):
            for layer_index in range(len(layers)):
                layer = layers[layer_index]
                nodes = layer.copy()
                positions = min_matrix[layer_index]
                if len(nodes) < 7:
                    best_total_distance = float("infinity")
                    best_combination = nodes
                    for combination in permutations(nodes,len(nodes)):
                        distance = 0
                        for index in range(len(combination)):
                            node_name = combination[index]
                            self.nodes[node_name].set_position(positions[index][0],positions[index][1])
                            distance += self.get_edges_size(node_name)
                        if distance < best_total_distance:
                            best_total_distance = distance
                            best_combination = combination
                    for index in range(len(best_combination)):
                        position = positions[index]
                        node_name = best_combination[index]
                        self.nodes[node_name].set_position(position[0],position[1])
                        matrix[position[0]][position[1]] = node_name
                else:
                    for position in positions:
                        best_distance = float("infinity")
                        best_node = None
                        for name in nodes:
                            self.nodes[name].set_position(position[0],position[1])
                            distance = self.get_edges_size(name)
                            if distance < best_distance:
                                best_distance = distance
                                best_node = name
                        if best_node is not None:
                            self.nodes[best_node].set_position(position[0],position[1])
                            nodes.remove(best_node)
                            matrix[position[0]][position[1]] = best_node
        return matrix

    def create_matrix_by_distance(self):
        layers = self.find_layer_orientation()
        next_position = 1 if len(layers[0]) % 2 == 0 else 1
        start = next_position
        end = next_position
        for node_name in layers[0]:
            self.nodes[node_name].set_position(1, next_position)
            if next_position > 0:
                start = next_position
                next_position = end - 2
            else:
                end = next_position
                next_position = start + 2
        if len(layers) > 1:
            for layer_index in range(1, len(layers)):
                positions = basic_positions(len(layers[layer_index]) + 2)
                for node_name in layers[layer_index]:
                    best_index = -1
                    best_distance = float("inf")
                    for position_index in range(0, len(positions)):
                        if is_possible(positions, position_index):
                            self.nodes[node_name].set_position(layer_index * 2 + 1, positions[position_index])
                            parents_distance = self.get_edges_size(node_name)
                            if best_distance > parents_distance:
                                best_index = position_index
                                best_distance = parents_distance
                    self.nodes[node_name].set_position(layer_index * 2 + 1, positions[best_index])
                    positions[best_index] = node_name
        lowest_index = float("inf")
        highest_index = -float("inf")
        for node_name in self.nodes:
            if self.nodes[node_name].position["j"] < lowest_index:
                lowest_index = self.nodes[node_name].position["j"]
            if self.nodes[node_name].position["j"] > highest_index:
                highest_index = self.nodes[node_name].position["j"]
        size = highest_index - lowest_index + 3
        for node_name in self.nodes:
            position = self.nodes[node_name].position
            self.nodes[node_name].set_position(position["i"], position["j"] - lowest_index + 1)
        matrix = [[0] * size]
        for layer in layers:
            matrix.append([0] * size)
            for node_name in layer:
                position = self.nodes[node_name].position
                matrix[position["i"]][position["j"]] = node_name
            matrix.append([0] * size)
        return matrix

    def get_movements(self, i, j, exception=None):
        if self.map is None:
            self.compile()
        if exception is None:
            exception = {"i": -1, "j": -1}
        movements = []
        if i < 0 or j < 0 or self.map is None:
            return movements
        for i1 in range(-1, 2):
            if 0 <= i1 + i < len(self.map):
                for j1 in range(-1, 2):
                    if 0 <= j1 + j < len(self.map[i1]) and \
                            (i1 != 0 or j1 != 0) and \
                            (type(self.map[i1 + i][j1 + j]) == int or
                             (exception["i"] == i1 + i and exception["j"] == j1 + j)):
                        movements.append({"i": i1 + i, "j": j1 + j,
                                          "distance": non_diagonal if i1 == 0 or j1 == 0 else diagonal})
        return movements

    def find_path(self, position: dict, target: dict, return_trace: bool = False):
        if self.map is None:
            self.compile()
        position["distance"] = 0
        paths = SortedPaths(Path(position, target))
        trace = []
        for row in self.map:
            trace.append([False] * len(row))
        trace[position["i"]][position["j"]] = True
        trace_movement = []
        while len(paths.list) > 0:
            if return_trace:
                trace_movement.append(trace)
            path = paths.pop(0)
            if path.path_list[-1]["i"] == target["i"] and path.path_list[-1]["j"] == target["j"]:
                if return_trace:
                    return path.path_list, trace_movement
                return path.path_list
            position = path.path_list[-1]
            movements = self.get_movements(position["i"], position["j"], target)
            for movement in movements:
                if movement not in path:
                    new_path = path.copy_add(movement)
                    paths_number = len(paths.list)
                    if paths_number == 0:
                        paths.add(new_path)
                        trace[movement["i"]][movement["j"]] = True
                    else:
                        paths.add(new_path)
                        trace[movement["i"]][movement["j"]] = True

    def get_edges_paths(self):
        if self.map is None:
            self.compile()
        paths = []
        for node_name in self.nodes:
            node = self.nodes[node_name]
            for target_name in node.children:
                target = self.nodes[target_name]
                node_position = node.position.copy()
                paths.append({"origin": node_name,
                              "target": target_name,
                              "path": self.find_path(node_position, target.position)})
        return paths

    def find_layer_orientation(self):
        self.set_parents()
        nodes = self.nodes.copy()
        defined_nodes = set([])
        next_nodes = set([])
        layers = []
        first = True
        while len(nodes) > 0 and (first or len(next_nodes) > 0):
            first = False
            next_nodes = set([])
            for node_name in nodes:
                if nodes[node_name].parents <= defined_nodes:
                    next_nodes.add(node_name)
            for defined_node_name in next_nodes:
                nodes.pop(defined_node_name, None)
                defined_nodes.add(defined_node_name)
            layers.append(list(next_nodes))
        if len(nodes) > 0:
            return None
        return layers

    def compile(self):
        self.map = self.create_matrix()

    def __iter__(self):
        if self.map is None:
            self.compile()
        nodes_dict = {}
        for node_name in self.nodes:
            node_dict = dict(self.nodes[node_name])
            node_dict.pop("name", None)
            nodes_dict[node_name] = node_dict
        yield "nodes", nodes_dict
        yield "edges", self.get_edges_paths()
        yield "height", len(self.map[0])
        yield "width", len(self.map)
