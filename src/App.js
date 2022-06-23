import React, { Component } from "react";
import Counters from "./Components/Products";
import Nav from "./Components/Navbar";

class App extends Component {
  state = {};

  render() {
    console.log(this.state.counters);
    return (<div>
      <Nav />
      <Counters />
      </div>
    );
  }
}

export default App;