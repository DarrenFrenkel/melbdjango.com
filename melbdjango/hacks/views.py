from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from hacks.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout

from .models import Idea, Vote
from .forms import IdeaForm, CommentForm

def idea_list(request):
    '''List all the Ideas!'''
    return render(request, 'hacks/idea_list.html', {
        'object_list': Idea.objects.with_total_votes().order_by('total_votes'),
    })

@login_required
def idea_add(request):
    '''Create a new Idea'''
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.owner = request.user
            idea.save()
            return redirect(idea)

    else:
        form = IdeaForm()

    return render(request, 'hacks/idea_form.html', {
        'form': form,
    })
    
def idea_detail(request, idea_id):
    '''Review an Idea'''
    idea = get_object_or_404(Idea, pk=idea_id)

    return render(request, 'hacks/idea_detail.html', {
        'idea': idea,
    })

@require_POST
def idea_vote(request, idea_id, direction):
    '''Cast a vote'''
    idea = get_object_or_404(Idea, pk=idea_id)
    url = idea.get_thank_you_url()
    try:
        with transaction.atomic():
            vote = Vote.objects.create(user=request.user, idea=idea, value=direction)
    except IntegrityError:
        messages.warning(request, 'You can only vote once on each idea.')
    else:
        messages.success(request, 'You %s voted %s!' % (vote.get_value_display(), idea))
    return redirect(url)

def idea_comment(request, idea_id):
    '''Post a comment on an Idea'''
    idea = get_object_or_404(Idea, pk=idea_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.idea = idea
            comment.user = request.user
            comment.save()
            return redirect(idea)

    else:
        form = CommentForm()

    return render(request, 'hacks/idea_comment.html', {
        'object': idea,
        'form': form,
    })

def idea_thank_you(request, idea_id):
    '''Thank you page for voting for an idea'''
    idea = get_object_or_404(Idea, pk=idea_id)
    return render(request, 'hacks/thank-you.html',{
        'idea': idea,
    } )	

def hacker_registration(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():		
            user = User.objects.create(username=form.cleaned_data['username'], email= form.cleaned_data['email'], password = form.cleaned_data['password'])	
            user.backend='django.contrib.auth.backends.ModelBackend'			
            user.save()
            login(request, user)			
            return redirect('/')
        else:
            return render(request, 'register.html', {'form':form})
    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form':form})		
	
def signin_request(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.get(username=form.cleaned_data['username'])
            hacker = authenticate(username=username, password=password)
            if hacker is not None:
                login(request, hacker)
                return render(request, 'index.html', {'form':form, 'user':user})
            else:
                return render(request, 'index.html', {'form':form})
        else:
                return render(request, 'index.html', {'form':form})		
    else:
        form = LoginForm()
        return render(request, 'index.html', {'form':form})		
	
def logout_request(request):
    logout(request)
    return redirect('/')	
