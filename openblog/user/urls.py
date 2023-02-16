from django.urls import path
from .views import *

urlpatterns=[
    path('uhome/',UserHome.as_view(),name="uhome"),
]