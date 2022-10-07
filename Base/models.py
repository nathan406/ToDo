from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Get(models.Model):
    activity = models.CharField(max_length=100,null=True,blank=False)
    description = models.TextField(null=True,blank=True,max_length=2000)
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated','-created']

    def __str__(self) :
        return self.activity

    def clean(self):
        if self.description:
            self.description = self.description.strip()

# class User(models.Model):
#     username = models.CharField(max_length=25,blank=False)
#     password = models.CharField(max_length=50)

#     def __str__(self) -> str:
#         return self.username
    
#     def __str__(self) -> str:
#         return self.password
 