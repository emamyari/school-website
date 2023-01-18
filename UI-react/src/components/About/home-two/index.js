// import React from 'react';
// import parse from "html-react-parser";
// // import aboutData from "../../../data/About/home-two";
// import aboutThumb from '../../../assets/img/about-2-bg.jpg'
// import {Link} from "react-router-dom";
// import axios from 'axios';

// const BaseUrl = "http://127.0.0.1:8000/AboutData/"
// const config = {
//     headers: {
//       accept: 'application/json',
//     },
//     data: {},
//   };

// const Initialization_AboutData = {
//     "title": "",
//     "heading": "",
//     "since": "",
//     "text": "",
//     "btnText": "",
//     "btnLink": "",
//     "thumb": "about-2.jpg"
// }

// const About = () => {

//     const [aboutData, setAboutData] = React.useState(Initialization_AboutData)
//     React.useEffect(() => {
//         axios.get(BaseUrl,config).then((Response) => {
//             setAboutData(Response.data)
//         })
//     })    



    
//     return (
//         <div className="home-two-about-area" style={{backgroundImage:`url(${aboutThumb})`}}>
//             <div className="container">
//                 <div className="row align-items-center">
//                     <div className="col-12 d-lg-none">
//                         <figure className="about-thumb">
//                             {/* <img src={require('../../../assets/img/' + aboutData.thumb)} alt="Businex-About"/> */}
//                         </figure>
//                     </div>

//                     <div className="col-lg-6">
//                         <div className="about-content about-content--2">
//                             <h6>{aboutData.title}</h6>
//                             <h2>{parse(aboutData.heading)}</h2>
//                             <span className="about-since">{aboutData.since}</span>
//                             <p>{parse(aboutData.text)}</p>
//                             <Link to={`${process.env.PUBLIC_URL + aboutData.btnLink}`} className="btn-about">{aboutData.btnText} <i className="fa fa-angle-double-left"/></Link>
                            
//                         </div>
//                     </div>
//                 </div>
//             </div>
//         </div>
//     );
// };

// export default About;
import React from 'react';
import axios from 'axios';

export default class PersonList extends React.Component {
  state = {
    persons: []
  }

  componentDidMount() {
    axios.get(`http://127.0.0.1:8000/AboutData/`)
      .then(res => {
        const persons = res.data;
        this.setState({ persons });
      })
  }

  render() {
    return (
      <ul>
        {
          this.state.persons
            .map(person =>
              <li key={person.title}>{person.text}</li>
            )
        }
      </ul>
    )
  }
}