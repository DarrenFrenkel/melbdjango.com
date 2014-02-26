from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class RegistrationForm(forms.Form):
    username = forms.CharField(label=u'User Name')
    email = forms.CharField(label=u'email')	
    password = forms.CharField(label=(u'Password'), widget = forms.PasswordInput(render_value=False))		
    password1 = forms.CharField(label=(u'Password'), widget = forms.PasswordInput(render_value=False))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
		    return username
        raise forms.ValidationError("That username is already taken, please select another username")

    def clean_password(self):
        if self.data['password'] != self.data['password1']:
            raise forms.ValidationError("The password doesn't match please try again")
        else:
            return self.data['password']	

class LoginForm(forms.Form):
    username = forms.CharField(label=(u'User Name'), max_length=30)
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False), max_length=30)		