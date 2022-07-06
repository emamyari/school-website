import React, { Component } from "react";
import Counters from "./Components/Products";
import Nav from "./Components/Navbar";

class App extends Component {
  state = {
    counters: [
      { id: 1, name: "Iphone", number: 3 },
      { id: 2, name: "Samsung", number: 1 },
      { id: 3, name: "Huawei", number: 7 },
      { id: 4, name: "Xiaomi", number: 9 },
      { id: 5, name: "Sony", number: 0 },
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
  componentDidMount() {
    fetch("http://192.168.1.116:7000/test/")
      .then(res => res.json())
      .then(
        (result) => {
          // this.setState({ counters: [result] })
        },
        (error) => {
        }
      )
  }

  render() {
    console.log(this.state.counters);
    return (<div>
      <Nav />
      <Counters counters={this.state.counters} onDelete={this.HandleDelete} onInc={this.HandleInc} onDec={this.HandleDec} />
    </div>
    );
  }
}

export default App;