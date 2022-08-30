import React from 'react';

const Sidebar = ({classes,children}) => {
    return (
        <div className={classes}>
            <div className="sidebar-wrap mt-sm-90 mt-md-100">
                {children}
            </div>
        </div>
    );
};

export default Sidebar;