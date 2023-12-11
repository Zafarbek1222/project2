from django.urls import path
from .views import HomePageView,AboutPageView,SinovPageView

urlpatterns=[
    path("sinov",SinovPageView.as_view(),name='sinov'),
    path("about",AboutPageView.as_view(),name='about'),
    path('',HomePageView.as_view(),name='home'),
]















