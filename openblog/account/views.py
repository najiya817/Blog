from django.shortcuts import render
from django.views.generic import View
from .forms import RegForm

# Create your views here.

class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"main_home.html")

class RegView(View):
    def get(self,request,*args,**kwargs):
        f=RegForm
        return render(request,"reg.html",{"form":f})
    
    def post(self,request,*args,**kwargs):
        form_data=RegForm(data=request.POST)
        if form_data=