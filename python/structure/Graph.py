import math

from structure.GraphNode import GraphNode
from structure.Path import Path, SortedPaths

diagonal = math.sqrt(2)
non_diagonal = 1


def distance_prediction(position, past_distance, target):
    future_distance = math.sqrt((position["i"] - target["i"]) ** 2 - (position["j"] - target["j"]) ** 2)
    return past_distance + future_distance


class Graph:
    def __init__(self):
        self.nodes = {}
        self.map = None

    def add_dict_node(self, name: str, data, children: []):
        node = GraphNode(name, data, children)
        self.add_node(node)

    def add_node(self, node: GraphNode):
        self.nodes[node.name] = node

    def set_parents(self):
        for node_name in self.nodes:
            for child in self.nodes[node_name].children:
                self.nodes[child].parents.add(node_name)

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
        for layer_index in range(len(layers)):
            layer = layers[layer_index]
            row = [0] * width
            layer_size = len(layer)
            if layer_size % 2 == 0:
                layer_size = layer_size + 1
            i = median - (layer_size - 1)
            for node_name in layer:
                row[i] = node_name
                self.nodes[node_name].set_position(layer_index * 2 + 1, i)
                i = i + 2
                if i == median and len(layer) % 2 == 0:
                    i = i + 2
            matrix.append(row)
            matrix.append([0] * width)
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
                    if paths_number == 0 and not trace[movement["i"]][movement["j"]]:
                        paths.add(new_path)
                        trace[movement["i"]][movement["j"]] = True
                    elif not trace[movement["i"]][movement["j"]]:
                        paths.add(new_path)
                        trace[movement["i"]][movement["j"]] = True
                    else:
                        for path_index in range(paths_number):
                            higher_cost_path = paths.list[path_index]
                            last_path_position = higher_cost_path.path_list[-1]
                            if movement["i"] == last_path_position["i"] and movement["j"] == last_path_position["j"]:
                                if higher_cost_path.best_distance > new_path.best_distance:
                                    paths.pop(path_index)
                                    paths.add(new_path)
                                break

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
