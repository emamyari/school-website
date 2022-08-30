import React from 'react';
const MemberInfo = ({teamMember}) => {
    const {profilePic,name,designation,bio,socials,address,phone,email,website} = teamMember;
    return (
        <div className="member-details-top">
            <div className="row">
                <div className="col-md-5">
                    <div className="member-pic mb-sm-35">
                        <img src={require('../../assets/img/' + profilePic)} alt={name}/>
                    </div>
                </div>

                <div className="col-md-7 ml-auto">
                    <div className="member-desc">
                        <h2>{name}</h2>
                        <h5>{designation}</h5>
                        <p dangerouslySetInnerHTML={{__html: bio}}/>

                        <div className="member-social-icons mt-25">
                            <a href={`https://facebook.com/${socials.facebook}`} target="_blank" rel="noopener noreferrer" className="facebook"><i className="fa fa-facebook"/></a>
                            <a href={`https://twitter.com/${socials.twitter}`} target="_blank" rel="noopener noreferrer" className="twitter"><i className="fa fa-twitter"/></a>
                            <a href={`https://linkedin.com/in/${socials.linkedin}`} target="_blank" rel="noopener noreferrer" className="linkedin"><i className="fa fa-linkedin"/></a>
                            <a href={`https://reddit.com/${socials.reddit}`} target="_blank" rel="noopener noreferrer" className="reddit"><i className="fa fa-reddit"/></a>
                            <a href={`https://pinterest.com/${socials.pinterest}`} target="_blank" rel="noopener noreferrer" className="pinterest"><i className="fa fa-pinterest"/></a>
                        </div>

                        <div className="contact-info mt-25">
                            <p><strong>آدرس</strong> <span dangerouslySetInnerHTML={{__html: address}}/></p>
                            <p><strong>تلفن</strong> {phone}</p>
                            <p><strong>ایمیل</strong> {email}</p>
                            <p><strong>سایت</strong> {website}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default MemberInfo;
