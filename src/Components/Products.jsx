import React, { Component } from "react";
import Counter from "./Product";
import "../components.css"

class Counters extends Component {

  render() {
    return (<div style={{ display: "flex" }}>
      <div style={{ width: "40%" }}></div>
      <div className="Products" s>
        {this.props.counters.map((c) => (
          <div className='Product'> 
            <Counter key={c.id} id={c.id} name={c.name} number={c.number} counter={c}
              onDelete={this.props.onDelete} onInc={this.props.onInc} onDec={this.props.onDec} />
          </div>
        ))
        }
      </div>
      <div style={{ width: "40%" }}></div>
    </div>);
  }
}

export default Counters