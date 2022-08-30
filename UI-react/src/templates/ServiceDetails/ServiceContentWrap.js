import React from 'react';
import SlickSlider from "../../components/UI/Slick";
import List from "../../components/UI/List";
import LI from "../../components/UI/List/Item";
import IconBox from "../../components/IconBox";
import Text from "../../components/UI/Text";

import HowWeWorksData from "../../data/HowWeWorks/how-we-works";

const ServiceContentWrap = ({service,totalService,prevService,nextService}) => {
    return (
        <div className="col-lg-8">
            <div className="service-details-content">
                <div className="service-thumbnail-wrapper">
                    <SlickSlider settings={{
                        className: "service-details-thumb",
                        arrows: false,
                        dots: true
                    }}>
                        {
                            service.previewImages.map((previewImg, indx) => (
                                <div key={indx}>
                                    <img src={require('../../assets/img/' + previewImg)} alt={service.title} />
                                </div>
                            ))
                        }
                    </SlickSlider>
                </div>

                <div className="service-details-info">
                    <h3>{service.title}</h3>
                    <p>{service.shortDesc}</p>

                    <div className="about-service mt-50 mt-sm-35">
                        <h4>درباره این خدمات</h4>
                        {
                            <div dangerouslySetInnerHTML={{__html: service.aboutServiceDesc}}/>
                        }
                        <List classes="service-feature mt-30">
                            {
                                service.features.map((feature,indx)=>(
                                    <LI key={indx}>{feature}</LI>
                                ))
                            }
                        </List>
                    </div>

                    <div className="how-we-works-wrap mt-50 mt-sm-35">
                        <h4>ما چگونه کار می کنیم؟</h4>
                        <Text styles={{marginBottom:20}}>
                            لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد.
                        </Text>

                        <div className="how-we-works-content service-details-page">
                            <div className="row">
                                {
                                    HowWeWorksData.map(iconbox=>(
                                        <IconBox
                                            key={iconbox.id}
                                            icon={iconbox.icon}
                                            title={iconbox.title}
                                            text={iconbox.text}
                                        />
                                    ))
                                }
                            </div>
                        </div>
                    </div>

                    <div className="pagination-wrap">
                        <ul className="pagination">
                            <li className="prev">
                                <a href={`${process.env.PUBLIC_URL + `/service/${prevService.title.split(' ').join('-').toLocaleLowerCase()}?id=${prevService.id}`}`}
                                   className={service.id === 1 ? "disabled" : null}
                                >
                                    <i className="fa fa-long-arrow-right"/> قبلی
                                </a>
                            </li>
                            <li className="next">
                                <a href={`${process.env.PUBLIC_URL + `/service/${nextService.title.split(' ').join('-').toLocaleLowerCase()}?id=${nextService.id}`}`}
                                   className={service.id === totalService ? "disabled" : null}
                                >
                                    بعدی <i className="fa fa-long-arrow-left"/>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ServiceContentWrap;
