# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response

def home_page(request):
	"""View for homepage"""
	return render_to_response('home_page.html', locals())

def login_page(request):
	"""View for the login page"""
	return HttpResponse('Login page placeholder. Need field for username'
		'password and password recovery link')

def logout_page(request):
	"""Place holder for logout page"""
	return HttpResponse('Place holder for logout page')

def signup_page(request):
	"""View for the signup page"""
	return HttpResponse('This is going to be the signup page. Need field for'
	'username, password, confirm password, email')

def user_page(request, username):
	"""View for user pages"""
	return HttpResponse('Place holder for userpage')
