import React, { Component } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'
import "../components.css"

class Counter extends Component {

    

    render() {
        return (<div>
            <p className="Title">{this.props.name}</p>

            <button onClick={() => this.props.onDec(this.props.counter)} className="btn btn-warning Dec" ><svg style={{ textAlign: "senter" }} width="20" height="20" fill="currentColor" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z" />
            </svg></button>

            <span className={"btn btn-info Count"}>{this.props.number}</span>

            <button onClick={() => this.props.onInc(this.props.counter)} className="btn btn-warning Inc"><svg style={{ textAlign: "senter" }} width="20" height="20" fill="currentColor" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M7.646 4.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1-.708.708L8 5.707l-5.646 5.647a.5.5 0 0 1-.708-.708l6-6z" />
            </svg></button>

            <button onClick={() => this.props.onDelete(this.props.id)} className="btn btn-warning Del"><svg width="17" height="17" fill="currentColor" viewBox="0 0 16 16">
              <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854Z" />
            </svg></button>
        </div>);
    }
}
export default Counter;