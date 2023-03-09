from django.shortcuts import redirect, render
from django.views.generic import View,CreateView,FormView,TemplateView
from .forms import RegForm,LogForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.mail import send_mail


# Create your views here.

class HomeView(TemplateView):
    template_name="main_home.html"
class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=User
    success_url=reverse_lazy('h')  
    def form_valid(self, form):
        send_mail(
            "welcome to openblog",
            "you are successfully registered to openblog",
            "najiyanaji817@gmail.com",
            [form.cleaned_data.get("email")]
        )
        messages.success(self.request,"registration successfull")
        self.object=form.save()
        return super().form_valid(form)
  
        
class LogView(FormView):
    form_class=LogForm
    template_name="log.html"
    def post(self,request,*args,**kwargs):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            pw=form_data.cleaned_data.get("password")
            user=authenticate(request,username=un,password=pw)
            if user:
                login(request,user)
                return redirect("uhome")
            else:
                return redirect("log")
        else:
            return render(request,"log.html",{"form":form_data})
        
class LogOutView(View):
    def get(self,request):
        logout(request)
        return redirect("log")

