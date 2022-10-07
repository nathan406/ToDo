from .models import Get,User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms



class GetForm(ModelForm):
    class Meta:
        model = Get
        widgets = {
            'activity': forms.TextInput(attrs={
                'placeholder': 'Activity',
                'class':'activity'
                }
                ),
            'description': forms.Textarea(
            attrs={'placeholder': 'about' ,
            'class':'body'}),
        }
        fields = ['activity','description']
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'activity',
                'class':'center-font'
                }
                ),
            'password': forms.Textarea(attrs={
                'placeholder': 'password' ,
                'class':'center-font'
                }
                )
            }