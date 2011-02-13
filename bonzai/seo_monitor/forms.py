# Django form classes go here

from django import forms

class RegistrationForm(forms.Form):
	"""Registration Form will verify password typed correctly."""
	username = forms.CharField(label=u'Username', max_lenght=30)
	email = forms.EmailField(label=u'Email')
	password1 = forms.Charfield(label=u'Password', widget=forms.PasswordInput())
	password2 = forms.Charfield(label=u'Password Again'. widget=forms.PasswordInput())
