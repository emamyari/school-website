import React, { Component } from "react";
import Counter from "./Product";
import "../components.css"

class Counters extends Component {

  render() {
    return (<div className="Products">
        {this.props.counters.map((c) => (
          <div className='Product'>
            <Counter key={c.id} id={c.id} name={c.name} number={c.number} maximum={c.maximum} counter={c}
              onDelete={this.props.onDelete} onInc={this.props.onInc} onDec={this.props.onDec} />
          </div>
        ))
        }
      </div>);
  }
}

export default Counters