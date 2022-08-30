import React,{Fragment} from 'react';
import Header from "../components/Header";
import ContactPage from "../templates/Contact";
import CallToAction from "../components/CallToAction";
import Footer from "../components/Footer";
import LoginRegister from "../components/LoginRegister";
import MobileMenu from "../components/MobileMenu";


const PageContact = () => {
    return (
        <Fragment>
            <Header/>
            <ContactPage/>
            <CallToAction/>
            <Footer/>
            <LoginRegister/>
            <MobileMenu/>
        </Fragment>
    );
};

export default PageContact;