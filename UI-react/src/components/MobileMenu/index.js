import React from 'react';
import OffCanvas from "../UI/OffCanvas";
import NavbarItem from "../Header/Navbar/NavbarItem";

const MobileMenu = () => {
    return (
        <OffCanvas type="menu">
            <div className="res-mobile-menu">
                <div className="mobile-nav">
                    <NavbarItem/>
                </div>
            </div>
        </OffCanvas>
    );
};

export default MobileMenu;