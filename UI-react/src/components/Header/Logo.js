import React, {Component} from 'react';
import logo from '../../assets/img/logo.png'

class Logo extends Component {
    render() {
        return (
            <div className="logo-area">
                <a href="/businex"><img src={logo} alt="Businex-Logo" /></a>
            </div>
        );
    }
}

export default Logo;
