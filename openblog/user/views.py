from django.shortcuts import render,redirect
from django.views.generic import View
from django.views.generic import TemplateView

# Create your views here.
class UserHome(TemplateView):
    template_name="userhome.html"