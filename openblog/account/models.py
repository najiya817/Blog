from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    age=models.IntegerField()
    options=(
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    )
    gender=models.CharField(max_length=100,choices=options,default="Male")
    phone=models.IntegerField()
    profile_pic=models.ImageField(upload_to="profile_pictures")
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="p_user")


class Blogs(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    image=models.ImageField(upload_to="blog_images")
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog")
    liked_by=models.ManyToManyField(User,related_name="likes",null=True)


class Comments(models.Model):
    comment=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="c_user")
    blog=models.ForeignKey(Blogs,on_delete=models.CASCADE,related_name="c_blog")