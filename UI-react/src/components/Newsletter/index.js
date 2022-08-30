import React from 'react';

const Newsletter = () => {
    return (
        <div className="sidebar-newsletter">
            <h3>خبرنامه</h3>
            <form action="#" method="post">
                <input type="email" placeholder="ایمیل شما"/>
                <button className="btn btn-brand">مشترک شدن</button>
            </form>
        </div>
    );
};

export default Newsletter;
