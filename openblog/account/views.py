from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import RegForm,LogForm
from django.contrib import messages

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
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"user registerd!!")
            return redirect("h")
        else:
            messages.error(request,"registration failed!!")
            return render(request,"reg.html",{"form":form_data})
        
class LogView(View):
    def get(self,request,*args,**kwargs):
        f=LogForm
        return render(request,"log.html",{"form":f})
    # def post(self,request,*args,**kwargs):

