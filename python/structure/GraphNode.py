class GraphNode:
    def __init__(self, node_name: str, data, output_into: [] = None):
        self.children = set(output_into) if output_into is not None else set([])
        self.parents = set([])
        self.data = data
        self.name = node_name
        self.position = None

    def set_position(self, i: int, j: int):
        self.position = {"i": i, "j": j}

    def __iter__(self):
        yield "name", self.name
        yield "children", list(self.children)
        yield "parents", list(self.parents)
        yield "data", self.data
        yield "position", self.position
