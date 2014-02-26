from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from . import models

class IdeaForm(forms.ModelForm):

    class Meta:
        model = models.Idea
        fields = (
            'title',
            'description',
        )

class CommentForm(forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = (
            'comment',
        )		