from django.urls import path
from .views import *

urlpatterns=[
    path('uhome/',UserHome.as_view(),name="uhome"),
    path('profile/',ProfileView.as_view(),name="pro"),
    path('addprofile/',AddProfile.as_view(),name="addpro"),

]