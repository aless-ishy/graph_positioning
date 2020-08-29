import React from 'react';
import Chip from "@material-ui/core/Chip";
import "../assets/NodeCard.scss";
import "../assets/Node.scss";
import edit from "../assets/create-white-36dp.svg";
import remove from "../assets/remove-white-36dp.svg";

class NodeCard extends React.Component {
    constructor(props) {
        super(props);
        this.makeChips = this.makeChips.bind(this);
    }

    makeChips() {
        const chips = [];
        if (this.props.children)
            for (let child of this.props.children)
                chips.push(<Chip color="secondary" key={child} label={child}/>)
        return chips;
    }

    render() {
        return (
            <div className="node-card">
                <div className="card-header">
                    <div className="button-container">
                        <div className="button-item" style={{backgroundColor: "rgb(97, 205, 187)"}}  onClick={this.props.onEdit}>
                            <img src={edit} alt={"edit-node"}/>
                        </div>
                    </div>
                    <div className="node">
                        <div className="node-item" style={{backgroundColor: "rgb(97, 205, 187)"}}>
                            <p>
                                {this.props.name}
                            </p>
                        </div>
                    </div>
                    <div className="button-container">
                        <div className="button-item" style={{backgroundColor: "rgb(244,117,96)"}} onClick={this.props.onRemove}>
                            <img src={remove} alt={"remove-node"}/>
                        </div>
                    </div>
                </div>
                <div className="card-content">
                    {this.makeChips()}
                </div>
            </div>
        );
    }
}

export default NodeCard;