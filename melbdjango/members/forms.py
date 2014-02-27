from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth import authenticate

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

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except:
            raise forms.ValidationError("Wrong Username")
        else:
            return username

    #def clean_password(self):
     #   username = self.cleaned_data['username']	
      #  password = self.cleaned_data['password']
       # u = User.objects.get(username=username)		
       # if not u.check_password(password):
        #    raise forms.ValidationError("Wrong Password")
        #else:
		 #    return password 			

         		 
	
	
	
	