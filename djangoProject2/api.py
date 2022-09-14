import json
from django.http import HttpResponse
from rest_framework.decorators import api_view




@api_view()

def Testomonialdata(request):
    data=[

            {
                "id": 1,
                "quote": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
                "author": "کاربر 100",
                "authorThumb": "testimonial/h-2-t-01.png",
                "designation": "مدیر فنی فیسبوک"
            },
            {
                "id": 2,
                "quote": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
                "author": "کاربر 200",
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




    return HttpResponse(json.dumps(data,default=lambda o:o.__dict__),content_type="application/json")

def Sliderdata(request):

    data=[
        {
            "id": 1,
            "title": "قالب ری اکت شرکتی",
            "text": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم adahagqdwydwvاز صنعت چاپ و با استفاده از طراحان گرافیک است.",
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
    return HttpResponse(json.dumps(data,default=lambda o:o.__dict__),content_type="application/json")

def Funfactdata(request):

    data=[
  {
    "id": 1,
    "counterNumber": 2654,
    "counterText": "مشتری راضیsgsgsg"
  },
  {
    "id": 2,
    "counterNumber": 1520,
    "counterText": "پروژه انجام شدهadawd"
  },
  {
    "id": 3,
    "counterNumber": 120,
    "counterText": "جایزه"
  },
  {
    "id": 4,
    "counterNumber": 3580,
    "counterText": "فنجان قهوه :)"
  }
]
    return HttpResponse(json.dumps(data,default=lambda o:o.__dict__),content_type="application/json")





