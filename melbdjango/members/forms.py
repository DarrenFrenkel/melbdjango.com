from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm 

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
		
class LoginForm(forms.Form):
    username = forms.CharField(label=(u'User Name'), max_length=30)
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False), max_length=30)
			