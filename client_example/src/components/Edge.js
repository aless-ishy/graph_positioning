import React from 'react';
import "../assets/Edge.scss";

const halfSide = 20;
const diagonal = Math.sqrt(2);

class Edge extends React.Component {
    render() {
        const edgeStyle = {opacity: this.props.opacity ? this.props.opacity : 1};
        const arrowStyle = {};
        if (this.props.transform) {
            const transform = this.props.transform;
            const x = transform.x ? transform.x : 0;
            const y = transform.y ? transform.y : 0;
            const rotate = this.props.transform.rotate;
            const scale = rotate % 2 !== 0 ? diagonal : 1;
            edgeStyle.transform = `translate(${x + halfSide}px,${y + halfSide}px) rotate(${rotate * 45}deg) scaleX(${scale})`;
            arrowStyle.transform = `translate(${x + halfSide - 15}px,${y + halfSide - 15}px) rotate(${rotate * 45}deg) translate(${rotate % 2 ? 25 : 8}px,0px)`;
        }
        return (
            <React.Fragment>
                <hr className="edge" style={edgeStyle}/>
                {this.props.children &&
                <div className="arrow-container" style={arrowStyle}>
                    {this.props.children}
                </div>
                }
            </React.Fragment>
        );
    }
}

export default Edge;