# Create your views here.

from django.http import HttpResponse

def home_page(request):
	"""View for homepage"""
	return HttpResponse('Welcome to the Home Page')

def login_page(request):
	"""View for the login page"""
	return HttpResponse('Login page placeholder. Need field for username'
		'password and password recovery link')

def logout_page(request):
	"""docstring for logout"""
	pass

def signup_page(request):
	"""View for the signup page"""
	return HttpResponse('This is going to be the signup page. Need field for'
	'username, password, confirm password, email')

