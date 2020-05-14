from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from json import JSONEncoder

class UserModel(models.Model):
    email = models.CharField(unique=True,max_length=100) 
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)   

    def __str__(self):
        return "name:{},password:{},email{}".format(self.name,self.password,self.email)     
    class Meta:
        ordering = ['created_on']
        def __unicode__(self):
            return self.title