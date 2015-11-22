from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class SignUp(TemplateView):
	template_name = 'users/signup.html'

class SignIn(TemplateView):
	template_name = 'users/signin.html'
