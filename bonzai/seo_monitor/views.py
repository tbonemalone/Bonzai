# Create your views here.

from django.http import HttpResponse

def home_page(request):
	"""View for homepage"""
	return HttpResponse('Welcome to the Home Page')

def signup(request):
	"""View for the signup page"""
	return HttpResponse('This is going to be the signup page. Need field for'
	'username, password, confirm password, email')

def login(request):
	"""View for the login page"""
	return HttpResponse('Login page placeholder. Need field for username'
		'password and password recovery link')