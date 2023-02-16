from django.shortcuts import render,redirect
from django.views.generic import View

# Create your views here.
class UserHome(View):
    def get(self,request,*args,**kwargs):
        return render(request,"userhome.html")
    