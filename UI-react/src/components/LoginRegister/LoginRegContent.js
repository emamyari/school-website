import React, {Fragment} from 'react';
import socialNetworks from "../../data/SocialNetworks/socials";

const LoginRegister = () => {
    return (
        <Fragment>
            <div className="off-canvas-item">
                <div className="log-in-content-wrap">
                    <h2>ورود</h2>
                    <div className="login-form mtn-15">
                        <form action="#" method="post">
                            <div className="form-input-item">
                                <label htmlFor="username" className="sr-only">نام کاربری</label>
                                <input type="text" id="username" placeholder="نام کاربری" required/>
                            </div>

                            <div className="form-input-item">
                                <label htmlFor="password" className="sr-only">رمز عبور</label>
                                <input type="password" id="password" placeholder="رمز عبور" required/>
                            </div>

                            <div className="form-input-item">
                                <button type="submit" className="btn-submit">ورود</button>
                            </div>
                        </form>
                    </div>

                    <div className="sign-up-notification">
                        <p>ثبت نام نکرده اید؟ <a href="/"> همین حالا ثبت نام کنید</a></p>
                    </div>
                </div>
            </div>

            <div className="off-canvas-item mt-sm-30">
                <div className="social-icons">
                    {
                        socialNetworks.map(social=>(
                            <a key={social.id} href={`https://${social.networkName}.com/${social.username}`} target="_blank" rel="noopener noreferrer">
                                <i className={`fa fa-${social.networkName}`}/>
                            </a>
                        ))
                    }
                </div>
                <div className="copyright-content">
                    <p>کپی رایت {new Date().getFullYear()} © تمامی حقوق برای بیزنکس محفوظ است. فارسی شده توسط <a href="https://www.rtl-theme.com/author/i-vira">قائم امیدی</a> </p>
                </div>
            </div>
        </Fragment>
    );
};

export default LoginRegister;
