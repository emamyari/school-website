import React, { Component } from "react";
import Counters from "./Components/Products";
import Table from "./Components/Table";
import Nav from "./Components/Navbar";
import HighchartsReact from "highcharts-react-official";
import Highcharts, { Series } from "highcharts";
import "./components.css"

class App extends Component {
  state = {
    counters: [
    ],
    highcharts_options: {
      chart: {
        type: 'column'
      },
      title: {
        text: 'counters'
      },
      xAxis: {
        type: 'category',
        labels: {
          rotation: 0,
          style: {
            fontSize: '15px',
            fontFamily: 'Comic Sans MS'
          }
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'number'
        }
      },
      legend: {
        enabled: false
      },
      series: [{
        name: 'number',
        data: [
          // ['Shanghai', 24.2],
          // ['Beijing', 20.8],
          // ['Karachi', 14.9],
          // ['Shenzhen', 13.7],
          // ['Guangzhou', 13.1],
          // ['Istanbul', 12.7],
          // ['Mumbai', 12.4],
          // ['Moscow', 12.2],
          // ['São Paulo', 12.0],
          // ['Delhi', 11.7],
          // ['Kinshasa', 11.5],
          // ['Tianjin', 11.2]
        ],
        dataLabels: {
          enabled: true,
          rotation: 0,
          color: '#FFFFFF',
          align: 'right',
          format: '{point.y:.1f}', // one decimal
          y: 25,
          x: -6,
          style: {
            fontSize: '13px',
            fontFamily: 'Comic Sans MS'
          }
        }
      }]
    }
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
    fetch("http://127.0.0.1:8000/sg/")
      .then(res => res.json())
      .then(
        (Counters) => {
          let Highcharts_Counters = []
          let i
          for (i in Counters) {
            Highcharts_Counters.push([Counters[i].name, Counters[i].number])
          }
          this.setState({ counters: Counters })
          this.setState({ highcharts_options: { series: [{ data: Highcharts_Counters }] } })
        },
        (error) => {
        }
      )

  }


  render() {
    return (<div>
      <Nav cd={this.state.counters.length} />
      <div style={{ display: "flex", margin: "2rem" }}>
        <Counters counters={this.state.counters} onDelete={this.HandleDelete} onInc={this.HandleInc} onDec={this.HandleDec} />
        <Table counters={this.state.counters} />
      </div>
      <HighchartsReact highcharts={Highcharts} options={this.state.highcharts_options} />
    </div>
    );
  }
}

export default App;