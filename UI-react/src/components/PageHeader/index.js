import React from 'react';

const PageHeader = ({bgImg,title,content}) => {
    return (
        <div className="page-header-area bg-img" style={{backgroundImage: `url(${bgImg})`}}>
            <div className="container">
                <div className="row">
                    <div className="col-lg-10 col-xl-8 m-auto text-center">
                        <div className="page-header-content-inner">
                            <div className="page-header-content">
                                <h2>{title}</h2>
                                <p>{content}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default PageHeader;