from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 

class RegistrationForm(UserCreationForm):
    email = forms.CharField(label=u'email')

    class Meta:
        model = User
        fields = [
            'username',
            'email',			
            'password1',
            'password2',			
		]
		
class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields= ['username', 'password']  		