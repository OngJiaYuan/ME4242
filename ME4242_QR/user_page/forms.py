from django import forms
 
# import GeeksModel from models.py
from .models import User
 
# create a ModelForm
class UserForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = User
        fields = "username"