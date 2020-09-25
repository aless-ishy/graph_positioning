import React from 'react';
import "../assets/Graph.scss";
import Node from "./Node";
import Edge from "./Edge";
import Arrow from "./Arrow";

class Graph extends React.Component {
    constructor(props) {
        super(props);
        this.drawNodes = this.drawNodes.bind(this);
        this.drawEdges = this.drawEdges.bind(this);
        this.setNode = this.setNode.bind(this);
        this.state = {};
    }

    setNode(node_name) {
        if (this.props.data && this.props.data.nodes) {
            const node = this.props.data.nodes[node_name]
            if (node) {
                const targets = {}
                for (let target of node.children)
                    targets[target] = true;
                this.setState({activeNode: node_name, targets})
            }
        }
    }

    drawNodes() {
        let nodes_components = [];
        if (this.props.data && this.props.data.nodes) {
            const nodes = this.props.data.nodes;
            for (let node_name in nodes)
                if (nodes.hasOwnProperty(node_name)) {
                    const node = nodes[node_name];
                    let color = "white";
                    if (this.state.activeNode === node_name)
                        color = "rgb(97, 205, 187)";
                    else if (this.state.targets && this.state.targets[node_name])
                        color = "rgb(244,117,96)";
                    nodes_components.push(<Node key={node_name}
                                                color={color}
                                                name={node_name}
                                                onMouseEnter={() => this.setNode(node_name)}
                                                transform={{x: node.position.i * 40, y: node.position.j * 40}}/>)
                }
        }
        return nodes_components;
    }

    drawEdges() {
        const firstLines = {};
        const edges_components = [];
        const arrow_components = {};
        if (this.props.data && this.props.data.edges) {
            const edges = this.props.data.edges;
            if (edges)
                for (let edge_index in edges)
                    if (edges.hasOwnProperty(edge_index) && edges[edge_index]) {
                        const edge = edges[edge_index].path;
                        const origin = edges[edge_index].origin;
                        const opacity = origin === this.state.activeNode ? 1.0 : 0.5;
                        let last_point;
                        if (edge)
                            for (let point_index = 0; point_index < edge.length; point_index++) {
                                const point = edge[point_index];
                                if (point_index !== 0) {
                                    const x = last_point.i * 40;
                                    const y = last_point.j * 40;
                                    const rotate = (point.j - last_point.j) * (last_point.i === point.i ? 2 : 1);
                                    const lineProperties = {x, y, rotate, opacity};
                                    const lineKey = `${x}${y}${rotate}`;
                                    if(point_index === edge.length - 1)
                                        arrow_components[lineKey] = true;
                                    if (!firstLines[lineKey])
                                        firstLines[lineKey] = [];
                                    if (opacity === 1)
                                        firstLines[lineKey].splice(0, 0, lineProperties)
                                    else
                                        firstLines[lineKey].push(lineProperties)
                                }
                                last_point = point;
                            }
                    }
        }
        for (let lineKey in firstLines) {
            if (firstLines.hasOwnProperty(lineKey)) {
                const line = firstLines[lineKey][0];
                edges_components.push(
                    <Edge key={lineKey}
                          transform={{x: line.x, y: line.y, rotate: line.rotate}} opacity={line.opacity}>
                        {line.opacity >= 1.0 && arrow_components[lineKey] && <Arrow/>}
                    </Edge>
                );
            }
        }
        return edges_components;
    }

    shouldComponentUpdate(nextProps, nextState, nextContext) {
        return this.props.data !== nextProps.data || this.state.activeNode !== nextState.activeNode;
    }

    render() {
        return (
            <div className="graph" style={this.props.data && {
                height: this.props.data.height * 40,
                width: this.props.data.width * 40,
            }}>
                {this.drawEdges()}
                {this.drawNodes()}
            </div>
        );
    }
}

export default Graph;