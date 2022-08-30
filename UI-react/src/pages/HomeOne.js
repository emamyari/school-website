import React, {Fragment} from 'react';

import Header from '../components/Header'
import Slider from '../components/Slider/home-one'
import About from '../components/About/home-one'
import Features from '../components/Features'
import Services from '../components/Services'
import Team from "../components/Team/home-one";
import Blog from "../components/Blog";
import BrandLogo from "../components/BrandLogo";
import Funfact from "../components/Funfact";
import CallToAction from "../components/CallToAction";
import Footer from "../components/Footer";
import Testimonials from "../components/Testimonials/home-one";
import LoginRegister from "../components/LoginRegister";
import MobileMenu from "../components/MobileMenu";

const HomeOne = () => {
    return (
        <Fragment>
            <Header/>
            <Slider/>
            <About/>
            <Features classes="sp-top"/>
            <Services classes="sm-top-wt"/>
            <Testimonials/>
            <Team/>
            <Blog/>
            <BrandLogo/>
            <Funfact/>
            <CallToAction/>
            <Footer/>
            <MobileMenu/>
            <LoginRegister/>
        </Fragment>
    );
};

export default HomeOne;