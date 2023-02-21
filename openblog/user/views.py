from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView
from .forms import *
from account .models import UserProfile
from django.contrib import messages
# Create your views here.
class UserHome(TemplateView):
    template_name="userhome.html"
class ProfileView(TemplateView):
    template_name="profile.html"  

class AddProfile(CreateView):
    template_name="addprofile.html"
    form_class=ProfieForm
    model=UserProfile
    success_url=reverse_lazy("pro")
    def form_valid(self,form):
        form.instance.user=self.request.user
        self.object=form.save()
        messages.success(self.request,"profile added")
        return super().form_valid(form)
# def post(self,req,*args,**kwargs):
    #     form_data=self.form_class(data=req.POST,files=req.FILES)
    #     if form_data.is_valid():
    #         form_data.instance.user=req.user
    #         form_data.save()
    #         return redirect("pro")
    #     else:
    #         return render(req,"addprofile.html",{"form":form_data})        
  