from django.contrib import admin
from django.urls import path
from controller.API import TestimonialData, SliderData, AboutData, ServicesData,sg
from controller.CallToActionData import CallToActionData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('TestimonialData/', TestimonialData),
    path('SliderData/', SliderData),
    path('AboutData/', AboutData),
    path('ServicesData/', ServicesData),
    path('CallToActionData/', CallToActionData),
    path('sg/', sg),
]
