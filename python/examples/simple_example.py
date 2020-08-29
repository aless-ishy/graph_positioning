import os
import sys

# Add structure location to path.
# Not needed if structure module is in the same location as this file or any file trying to import structure
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from structure.Graph import Graph

if __name__ == '__main__':
    some_data = None
    graph = Graph()
    graph.add_dict_node("1", some_data, ["2", "3", "4", "5"])
    graph.add_dict_node("2", some_data, ["5"])
    graph.add_dict_node("3", some_data, ["5"])
    graph.add_dict_node("4", some_data, ["3"])
    graph.add_dict_node("5", some_data, [])

    # Sets implicit attributes, like parents or nodes positions in matrix.
    # Needs to be compiled every time a node is added.
    graph.compile()
    print(graph.find_path({"i": 0, "j": 0}, {"i": 1, "j": 1}))
