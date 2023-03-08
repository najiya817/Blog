from django.urls import path
from .views import *

urlpatterns=[
    path('uhome/',UserHome.as_view(),name="uhome"),
    path('profile/',ProfileView.as_view(),name="pro"),
    path('addprofile/',AddProfile.as_view(),name="addpro"),
    path('cpass/',CPassView.as_view(),name="cpassd"),
    path('ep/<int:pk>',EditPro.as_view(),name="ep"),
    path('myb/',MyBlogView.as_view(),name="myb"),
    path('delblg/<int:pk>',DeleteBlog.as_view(),name="delblg"),
    path('edtblg/<int:pk>',EditBlog.as_view(),name="edtblg"),
    path('cadd/<int:bid>',commentadd,name="cmnt"),
    path('like/<int:bid>',addlike,name="like"),


]