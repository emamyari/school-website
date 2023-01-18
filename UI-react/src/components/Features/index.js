import React from 'react';
import Feature from './FeatureItem'
// import FeaturesData from '../../data/Features/features'
import axios from 'axios';

function Features({classes}) {
    const BaseUrl = "http://127.0.0.1:8000/FeaturesData/"
    const [FeaturesData, setfea] = React.useState([])
    React.useEffect(() => {
        axios.get(BaseUrl).then((Response) => {
            setfea(Response.data)
        })
    })  

    return (
        <div className={`feature-area-wrapper ${classes}`}>
            <div className="container">
                <div className="row mtn-sm-60 mtn-md-5">
                    {
                        FeaturesData.map(feature=>(
                            <Feature key={feature.id} title={feature.title} text={feature.text} img={feature.imgSrc} />
                        ))
                    }
                </div>
            </div>
        </div>
    );
}

export default Features;