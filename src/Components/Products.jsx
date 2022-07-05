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

  HandleInc = (counter) => {
    const counters = [...this.state.counters]
    const index = counters.indexOf(counter)
    counters[index] = { ...counter }
    counters[index].number++;
    this.setState({ counters })
  }

  HandleDec = (counter) => {
    const counters = [...this.state.counters]
    const index = counters.indexOf(counter)
    counters[index] = { ...counter }
    if (counters[index].number > 0) {
      counters[index].number--;
    }
    this.setState({ counters })
  }

  render() {
    return (<div style={{ display: "flex" }}>
      <div style={{ width: "40%" }}></div>
      <div className="Products" s>
        {this.state.counters.map((c) => (
          <div className='Product'>
            <Counter number={c.number} id={c.id} key={c.id} name={c.value} counter={c}
              onDelete={this.HandleDelete} onInc={this.HandleInc} onDec={this.HandleDec} />
          </div>
        ))
        }
      </div>
      <div style={{ width: "40%" }}></div>
    </div>);
  }
}

export default Counters