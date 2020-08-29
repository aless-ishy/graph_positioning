import React from 'react';
import "../assets/Node.scss";
class Node extends React.Component {
    render() {
        const divProps = {...this.props}
        delete divProps.transform;
        delete divProps.name;
        delete divProps.key;
        let style = {}
        if(this.props.transform) {
            const transform = this.props.transform;
            const x = transform.x ? transform.x : 0;
            const y = transform.y ? transform.y : 0;
            style.transform = `translate(${x}px,${y}px)`
        }
        return (
            <div className="node" style={style}>
                <div className="node-item" {...divProps} style={{backgroundColor:this.props.color ? this.props.color : "white"}}>
                    <p>
                        {this.props.name}
                    </p>
                </div>
            </div>
        );
    }
}

export default Node;