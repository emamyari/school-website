import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from controller.testimonia import DAO
from controller.SliderData import MMD
from controller.AboutData import About
from controller.CallToActionData import CallToActiondata
@api_view(['''GET'''])
def TestimonialData(request):
    data = DAO()
    return HttpResponse(json.dumps(data), content_type='''application/json''')


@api_view(['''GET'''])
def SliderData(request):
    data = MMD()
    return HttpResponse(json.dumps(data), content_type='application/json')


@api_view(['''GET'''])
def AboutData(request):
    data = About()
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
    data = CallToActiondata()
    return HttpResponse(json.dumps(data), content_type='application/json')
