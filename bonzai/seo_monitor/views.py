# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout 
from django.shortcuts import render_to_response

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
	return HttpResponse('This is going to be the signup page. Need field for'
	'username, password, confirm password, email')

def user_page(request, username):
	"""View for user pages"""
	return render_to_response('user_page.html')
	
