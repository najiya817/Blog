from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import *
from account .models import UserProfile
from .forms import ProfileForm
from django.contrib import messages
from  django.contrib.auth import authenticate,login,logout



# Create your views here.
class UserHome(TemplateView):
    template_name="userhome.html"
class ProfileView(TemplateView):
    template_name="profile.html"  

class AddProfile(CreateView):
    template_name="addprofile.html"
    form_class=ProfileForm
    model=UserProfile
    success_url=reverse_lazy("pro")
    def form_valid(self,form):
        form.instance.user=self.request.user
        self.object=form.save()
        messages.success(self.request,"profile added")
        return super().form_valid(form)
# def post(self,req,*args,**kwargs):
#         form_data=self.form_class(data=req.POST,files=req.FILES)
#         if form_data.is_valid():
#             form_data.instance.user=req.user
#             form_data.save()
#             return redirect("pro")
#         else:
#             return render(req,"addprofile.html",{"form":form_data})       

class CPassView(FormView):
    template_name="cpass.html"
    form_class=CPassForm
    def post(self,request,*args,**kwargs):
        form=self.form_class(data=request.POST)
        if form.is_valid():
            old=form.cleaned_data.get("old_pass")
            new=form.cleaned_data.get("new_pass")
            cnf=form.cleaned_data.get("confirm_pass")
            user=authenticate(request,username=request.user.username,password=old)
            if user:
                if new==cnf:
                    user.set_password(new)
                    user.save()
                    logout(request)
                    messages.success(request,"password changed")
                    return redirect("log")
                else:
                    messages.error(request,"passwords mismatch")
                    return redirect("cpass")
            else:
                messages.error(request,"old password enterd is incorrect")
                return redirect("cpass")