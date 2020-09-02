# # if not building with docker
# import os
# import sys
# # Add structure location to path.
# # Not needed if structure module is in the same location as this file or any file trying to import structure
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from flask import Flask, render_template, request
from structure.Graph import Graph

app = Flask(__name__)

# Allows access to the server with node and react development
# from flask_cors import CORS
# CORS(app)

graph = Graph()


@app.route("/")
def index():
    global graph
    graph = Graph()
    return render_template("index.html")


@app.route("/api/delete")
def delete():
    global graph
    graph = Graph()
    return "200"


@app.route("/api/get_example")
def get_example():
    some_data = None
    graph_example = Graph()
    graph_example.add_dict_node("A", some_data, ["B"])
    graph_example.add_dict_node("B", some_data, ["C"])
    graph_example.add_dict_node("C", some_data, ["D"])
    graph_example.add_dict_node("D", some_data, [])
    return dict(graph_example)


@app.route("/api/compile", methods=["POST"])
def compile_graph():
    json = request.json
    if "nodes" in json:
        nodes = json["nodes"]
        if len(nodes):
            graph_response = Graph()
            for node_name in nodes:
                graph_response.add_dict_node(node_name, None, nodes[node_name])
            return dict(graph_response)
    return {"error": "Not Valid"}


if __name__ == '__main__':
    app.run()
