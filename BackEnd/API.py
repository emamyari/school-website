import json
from rest_framework.decorators import api_view
from django.http import HttpResponse


@api_view(['''GET'''])
def TestimonialData(request):
    data = [
        {
            "id": 1,
            "quote": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "author": "کاربر 1000",
            "authorThumb": "testimonial/h-2-t-01.png",
            "designation": "مدیر فنی فیسبوک"
        },
        {
            "id": 2,
            "quote": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "author": "کاربر 2",
            "authorThumb": "testimonial/h-2-t-02.png",
            "designation": "موسس علی بابا"
        },
        {
            "id": 3,
            "quote": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "author": "کاربر 3",
            "authorThumb": "testimonial/h-2-t-03.png",
            "designation": "مدیر اجرایی دیجی کالا"
        }
    ]
    return HttpResponse(json.dumps(data), content_type='''application/json''')


@api_view(['''GET'''])
def SliderData(request):
    data = [
        {
            "id": 1,
            "title": "قالب ری اکت شرکتی",
            "text": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "bg": "slider/h-2-01.jpg",
            "btnText": "اطلاعات بیشتر",
            "btnLink": "/about"
        },
        {
            "id": 2,
            "title": "پول خود را هدر ندهید",
            "text": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "bg": "slider/h-2-02.jpg",
            "btnText": "اطلاعات بیشتر",
            "btnLink": "/about"
        }
    ]
    return HttpResponse(json.dumps(data), content_type='application/json')


@api_view(['''GET'''])
def AboutData(request):
    data = {
        "title": "درباره ما",
        "heading": "ما کسب و کار شما را به یک کسب و کار حرفه ای تبدیل می کنیم",
        "since": "از سال 1390",
        "text": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد.",
        "btnText": "اطلاعات بیشتر",
        "btnLink": "/about",
        "thumb": "about-2.jpg"
    }
    return HttpResponse(json.dumps(data), content_type='application/json')


@api_view(['''GET'''])
def ServicesData(request):
    data = [
        {
            "id": 1,
            "title": "ایده های خلاقانه",
            "shortDesc": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "thumb": "service/01.jpg",
            "previewImages": [
                "service/details/01.jpg",
                "service/details/02.jpg",
                "service/details/03.jpg"
            ],
            "aboutServiceDesc": "<p>لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد.</p>",
            "features": [
                "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 1",
                "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 2"
            ]
        },
        {
            "id": 2,
            "title": "راهکارهای دیجیتال",
            "shortDesc": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "thumb": "service/02.jpg",
            "previewImages": [
                "service/details/01.jpg",
                "service/details/02.jpg",
                "service/details/03.jpg"
            ],
            "aboutServiceDesc": "<p>لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد.</p>",
            "features": [
                "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 1",
                "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 2"
            ]
        },
        {
            "id": 3,
            "title": "برندینگ و ارتباط",
            "shortDesc": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "thumb": "service/03.jpg",
            "previewImages": [
                "service/details/01.jpg",
                "service/details/02.jpg",
                "service/details/03.jpg"
            ],
            "aboutServiceDesc": "<p>لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد.</p>",
            "features": [
                "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 1",
                "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 2"
            ]
        },
        {
            "id": 4,
            "title": "استراتژی های خلاقانه",
            "shortDesc": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "thumb": "service/04.jpg",
            "previewImages": [
                "service/details/01.jpg",
                "service/details/02.jpg",
                "service/details/03.jpg"
            ],
            "aboutServiceDesc": "<p>لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد.</p>",
            "features": [
                "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 1",
                "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 2"
            ]
        },
        {
            "id": 5,
            "title": "سیاست بازاریابی",
            "shortDesc": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "thumb": "service/05.jpg",
            "previewImages": [
                "service/details/01.jpg",
                "service/details/02.jpg",
                "service/details/03.jpg"
            ],
            "aboutServiceDesc": "<p>لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد.</p>",
            "features": [
                "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 1",
                "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 2"
            ]
        },
        {
            "id": 6,
            "title": "کمپین های مختلف",
            "shortDesc": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "thumb": "service/06.jpg",
            "previewImages": [
                "service/details/03.jpg",
                "service/details/01.jpg",
                "service/details/02.jpg"
            ],
            "aboutServiceDesc": "<p>لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد.</p>",
            "features": [
                "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 1",
                "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 2"
            ]
        }
    ]
    return HttpResponse(json.dumps(data), content_type='application/json')


@api_view(['''GET'''])
def CallToActionData(request):
    data = {
        "title": "همین امروز شروع کنید",
        "text": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
        "btnText": "تماس با ما",
        "btnLink": "/contact"
    }
    return HttpResponse(json.dumps(data), content_type='application/json')
