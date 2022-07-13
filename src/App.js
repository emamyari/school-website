import React, { Component } from "react";
import Counters from "./Components/Products";
import Table from "./Components/Table";
import Nav from "./Components/Navbar";

class App extends Component {
  state = {
    counters: [
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
    if (counters[index].number < counters[index].maximum) {
      counters[index].number++;
    }
    this.setState({ counters })
  }

  HandleDec = (counter) => {
    const counters = [...this.state.counters]
    const index = counters.indexOf(counter)
    counters[index] = { ...counter }
    if (counters[index].number > 1) {
      counters[index].number--;
    }
    this.setState({ counters })
  }
  componentDidMount() {

    fetch("http://127.0.0.1:8000/gc/")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({ counters: result })
          // console.log(result)
        },
        (error) => {
        }
      )

  }


  render() {
    // console.log(this.state.counters);
    return (<div>
      <Nav cd={this.state.counters.length} />
      <div style={{ display: "flex",margin: "2rem" }}>
        <Counters counters={this.state.counters} onDelete={this.HandleDelete} onInc={this.HandleInc} onDec={this.HandleDec} />
        <Table counters={this.state.counters} />
      </div>
    </div>
    );
  }
}

export default App;