import React from 'react';
import './assets/App.css';
import Graph from "./components/Graph";
import TextField from "@material-ui/core/TextField";
import Chip from "@material-ui/core/Chip";
import Button from "@material-ui/core/Button";
import NodeCard from "./components/NodeCard";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            children: [],
            node_name: "",
            child: "",
            nodes: {}
        };
        this.addChild = this.addChild.bind(this);
        this.addNode = this.addNode.bind(this);
        this.createNodeCards = this.createNodeCards.bind(this);
        this.removeChild = this.removeChild.bind(this);
        this.removeNode = this.removeNode.bind(this);
        this.editNode = this.editNode.bind(this);
        this.compileGraph = this.compileGraph.bind(this);
        this.clean = this.clean.bind(this);
    }

    clean(){
        this.setState({
            children: [],
            node_name: "",
            child: "",
            nodes: {}});
    }

    compileGraph() {
        const nodes = this.state.nodes;
        if (Object.keys(nodes).length > 0) {
            const request = {
                method: 'POST',
                mode: 'cors',
                cache: 'no-cache',
                credentials: 'same-origin',
                headers: {
                    'Content-Type': 'application/json'
                },
                redirect: 'follow',
                referrerPolicy: 'no-referrer',
                body: JSON.stringify({nodes})
            };
            fetch("/api/compile", request)
                .then(response => response.json())
                .then(response => {
                    if (!response.error) {
                        this.setState({graph: response});
                    }
                });
        }
    }

    addNode() {
        if (this.state.node_name !== "") {
            const nodes = this.state.nodes;
            nodes[this.state.node_name] = [...this.state.children];
            this.setState({children: [], node_name: "", child: "", nodes});
        }
    }

    createNodeCards() {
        const cards = []
        const nodes = this.state.nodes;
        for (let node_name in nodes)
            if (nodes.hasOwnProperty(node_name))
                cards.push(<NodeCard key={node_name} name={node_name} children={nodes[node_name]}
                                     onRemove={() => this.removeNode(node_name)}
                                     onEdit={() => this.editNode(node_name)}/>)
        return cards;
    }

    addChild(e) {
        if (e.key !== "Enter")
            return;
        const children = this.state.children;
        const child = this.state.child;
        if (child !== "" && !children.includes(child)) {
            children.push(child);
            this.setState({children, child: ""})
        }
    }

    removeChild(node_name) {
        const children = this.state.children;
        const index = children.indexOf(node_name);
        if (index > -1) {
            children.splice(index, 1);
            this.setState({children})
        }
    }

    removeNode(node_name) {
        const nodes = this.state.nodes;
        if (nodes[node_name]) {
            delete nodes[node_name];
            this.setState({nodes})
        }
    }

    editNode(node_name) {
        const nodes = this.state.nodes;
        if (nodes[node_name]) {
            const nodeChildren = nodes[node_name];
            delete nodes[node_name];
            this.setState({nodes, children: nodeChildren, node_name: node_name})
        }
    }

    componentDidMount() {
        fetch("/api/get_example")
            .then(response => response.json())
            .then(response => this.setState({graph: response}));
    }

    render() {
        return (
            <div className="App">
                <h2>Graph Display</h2>
                <div className="actions">
                    <div className="form">
                        <TextField id="node_name" style={{width: 90}} label="Node Name" value={this.state.node_name}
                                   onChange={e => this.setState({node_name: e.target.value})}/>
                        <TextField id="child" style={{width: 90}} label="Add Child" value={this.state.child}
                                   onChange={e => this.setState({child: e.target.value})} onKeyPress={this.addChild}/>
                    </div>
                    <div style={{width: 40}}/>
                    <div>
                        <h3>Children</h3>
                        <div className="children-panel">
                            {this.state.children.map(node_name => <Chip key={node_name}
                                                                        onDelete={() => this.removeChild(node_name)}
                                                                        label={node_name}/>)}
                        </div>
                    </div>
                </div>
                <div className="action-buttons">
                    <Button variant="contained" color="secondary" onClick={this.addNode}>Add Node</Button>
                    <Button variant="contained" color="secondary" onClick={this.clean}>Clean</Button>
                    <Button variant="contained" color="secondary" disabled={Object.keys(this.state.nodes).length < 1} onClick={this.compileGraph}>Compile</Button>
                </div>
                <div className="node-cards">
                    {this.createNodeCards()}
                </div>
                <div className="App-content">
                    <Graph data={this.state.graph}/>
                </div>
            </div>
        );
    }
}

export default App;
