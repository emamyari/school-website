import React, { Component } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'
import "../components.css"

class Counter extends Component {
    state = { count: this.props.number }

    HandleInc = () => {
        var copy = this.state.count
        var set_count = copy >= 10 ? this.state.count : this.state.count + 1
        this.setState({ count: set_count })
    }

    HandleDec = () => {
        var copy = this.state.count
        var set_count = copy <= 0 ? this.state.count : this.state.count - 1
        this.setState({ count: set_count })
    }

    render() {
        return (<div>
            <p className="Title">{this.props.name}</p>

            <button onClick={this.HandleDec} className="btn btn-warning Dec" ><svg style={{ textAlign: "senter" }} width="20" height="20" fill="currentColor" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z" />
            </svg></button>

            <span className={"btn btn-info Count"}>{this.state.count}</span>

            <button onClick={this.HandleInc} className="btn btn-warning Inc"><svg style={{ textAlign: "senter" }} width="20" height="20" fill="currentColor" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M7.646 4.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1-.708.708L8 5.707l-5.646 5.647a.5.5 0 0 1-.708-.708l6-6z" />
            </svg></button>
        </div>);
    }
}
export default Counter;
function sas() {}