# Create your views here.

from django.http import HttpResponse

def home_page(request):
	"""Place holder view for homepage"""
	return HttpResponse('Welcome to the Home Page')