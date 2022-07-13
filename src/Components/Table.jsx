import React, { Component } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'
import "../components.css"
class Table extends Component {
    state = {}
    render() {
        return (<table className="table-Products">
            <tr id="t-head" className="table-Products-head">
                <td>ID</td>
                <td>Name</td>
                <td>Number</td>
                <td>Maximum</td>
            </tr>
            {this.props.counters.map((c) => (
                <tr>
                    <td>{c.id}</td>
                    <td>{c.name}</td>
                    <td>{c.number}</td>
                    <td>{c.maximum}</td>
                </tr>
            ))
            }
        </table>);
    }
}

export default Table;