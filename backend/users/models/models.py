from django.db import models
from django.forms import ModelForm
from core.models import abstract_model

class UserModel(abstract_model.AbstractBasicModel):
    email = models.CharField(unique=True,max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    def __str__(self):
        return "name:{},password:{},email{}".format(self.name,self.password,self.email)
    class Meta:
        ordering = ['name']
        def __unicode__(self):
            return self.title
            
class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['name', 'email', 'password']