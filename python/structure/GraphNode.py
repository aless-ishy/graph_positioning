class GraphNode:
    def __init__(self, node_name: str, layer_list: [], output_into: [] = None):
        self.children = set(output_into) if output_into is not None else set([])
        self.parents = set([])
        self.layer_list = layer_list
        self.name = node_name
        self.position = None

    def set_position(self, i: int, j: int):
        self.position = {"i": i, "j": j}

    def __iter__(self):
        yield "name", self.name
        yield "children", list(self.children)
        yield "parents", list(self.parents)
        yield "layer_list", self.layer_list
        yield "position", self.position
