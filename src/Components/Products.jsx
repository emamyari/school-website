import React, { Component } from "react";
import Counter from "./Product";
import "../components.css"

class Counters extends Component {
  state = {
    counters: [
      { id: 1, value: "Iphone", number: 3 },
      { id: 2, value: "Samsung", number: 1 },
      { id: 3, value: "Huawei", number: 7 },
      { id: 4, value: "Xiaomi", number: 9 },
      { id: 5, value: "Sony", number: 0 },
    ],
  };

  HandleDelete = (counterId) => {
    const counters = this.state.counters.filter(c => c.id != counterId)
    this.setState({ counters })
  }

  render() {
    return (<div style={{ display: "flex" }}>
      <div style={{ width: "40%" }}></div>
      <div className="Products" s>
        {this.state.counters.map((c) => (
          <div className='Product'>
            <Counter number={c.number} key={c.id} name={c.value} />
            <button onClick={() => this.HandleDelete(c.id)} className="btn btn-warning Del"><svg width="17" height="17" fill="currentColor" viewBox="0 0 16 16">
              <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854Z" />
            </svg></button>
          </div>
        ))
        }
      </div>
      <div style={{ width: "40%" }}></div>
    </div>);
  }
}

export default Counters