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

    def add_dict_node(self, name: str, layer_list: [], children: []):
        node = GraphNode(name, layer_list, children)
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
        width = largest_layer_size * 2 - 1
        median = int(width * 0.5)
        matrix = []
        for layer_index in range(len(layers)):
            layer = layers[layer_index]
            row = [0] * width
            layer_size = len(layer)
            if layer_size % 2 == 0:
                layer_size = layer_size + 1
            i = median - (layer_size - 1)
            for node_name in layer:
                row[i] = node_name
                self.nodes[node_name].set_position(layer_index * 2, i)
                i = i + 2
                if i == median and len(layer) % 2 == 0:
                    i = i + 2
            matrix.append(row)
            if layer_index < len(layers) - 1:
                matrix.append([0] * width)
        return matrix

    def get_movements(self, i, j, exception=None):
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

    def find_path(self, position: dict, target: dict):
        print("Position ", position)
        print("Target ", target)
        paths = SortedPaths(Path(position, target))
        trace = []
        for row in self.map:
            trace.append([False] * len(row))
        trace[position["i"]][position["j"]] = True
        while len(paths.list) > 0:
            matrix = trace
            s = [[str(int(e)) for e in row] for row in matrix]
            lens = [max(map(len, col)) for col in zip(*s)]
            fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
            table = [fmt.format(*row) for row in s]
            print('\n'.join(table))
            print("\n")
            path = paths.pop(0)
            if path.path_list[-1]["i"] == target["i"] and path.path_list[-1]["j"] == target["j"]:
                return path
            position = path.path_list[-1]
            movements = self.get_movements(position["i"], position["j"], target)
            for movement in movements:
                if movement not in path:
                    new_path = path.add_with_copy(movement)
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

    def create_map(self):
        self.map = self.create_matrix()
        paths = []
        for node_name in self.nodes:
            node = self.nodes[node_name]
            for target_name in node.children:
                target = self.nodes[target_name]
                node_position = node.position.copy()
                node_position["distance"] = 0
                paths.append({"origin": node_name,
                              "target": target_name,
                              "path": self.find_path(node_position, target.position)})
        for path in paths:
            if len(path["path"].path_list) > 2:
                for movement in path["path"].path_list[1:-1]:
                    self.map[movement["i"]][movement["j"]] = path["origin"] + "E"
        return self.map

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

    def __iter__(self):
        yield "layers_orientation", self.find_layer_orientation()

        nodes_dict = {}
        for node_name in self.nodes:
            nodes_dict[node_name] = dict(self.nodes[node_name])

        yield "nodes", nodes_dict
