from django import forms
from account.models import UserProfile,Blogs

class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=['user']

class CPassForm(forms.Form):
    old_pass=forms.CharField(max_length=100,label="old password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter old password"}))
    new_pass=forms.CharField(max_length=100,label="new password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter new password"}))
    confirm_pass=forms.CharField(max_length=100,label="confirm password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm new password"}))


class BlogForm(forms.ModelForm):
    class Meta:
        model=Blogs
        fields=["title","description","image"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"Title..."}),
            "description":forms.Textarea(attrs={"class":"form-control","placeholder":"Description...."}),
            "image":forms.FileInput(),
            
        }