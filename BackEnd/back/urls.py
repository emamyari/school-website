from django.contrib import admin
from django.urls import path
from API import TestimonialData, SliderData, AboutData, ServicesData, CallToActionData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('TestimonialData/', TestimonialData),
    path('SliderData/', SliderData),
    path('AboutData/', AboutData),
    path('ServicesData/', ServicesData),
    path('CallToActionData/', CallToActionData),
]
