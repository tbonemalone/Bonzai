# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import logout 
from django.shortcuts import render_to_response
from seo_monitor.forms import RegistrationForm
from django.contrib.auth.models import User

def home_page(request):
	"""View for homepage"""
	other = request.META
	return render_to_response('home_page.html', {'user': request.user, 'other': other})

def logout_page(request):
	"""Place holder for logout page"""
	logout(request)
	return HttpResponseRedirect("/")

def signup_page(request):
	"""View for the signup page"""
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password1'],
				email=form.cleaned_data['email']
			)
			return HttpResponseRedirect('/')
	else:
		form = RegistrationForm()
	variables = RequestContext(request, {'form': form})
	return render_to_response('registration/signup_page.html', variables)

def user_page(request, username):
	"""View for user pages"""
	user = User.objects.get(username=username)
	username = user.username
	email = user.email
	return render_to_response('user_page.html', {'username': username, 'email': email })
	
