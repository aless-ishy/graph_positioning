import React from 'react';
import "../assets/Edge.scss";

const halfSide = 20;
const diagonal = Math.sqrt(2);

class Edge extends React.Component {
    render() {
        let style = {opacity: this.props.opacity ? this.props.opacity : 1}
        if(this.props.transform) {
            const transform = this.props.transform;
            const x = transform.x ? transform.x : 0;
            const y = transform.y ? transform.y : 0;
            const rotate = this.props.transform.rotate;
            const scale = rotate % 2 !== 0 ? diagonal : 1;
            style.transform = `translate(${x + halfSide}px,${y + halfSide}px) rotate(${rotate*45}deg) scaleX(${scale})`;
        }
        return (
            <hr className="edge" style={style}/>
        );
    }
}

export default Edge;