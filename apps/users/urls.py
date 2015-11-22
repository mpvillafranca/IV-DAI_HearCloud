from django.conf.urls import patterns,include, url
from .views import SignUp,SignIn

urlpatterns = patterns('',
	url(r'^signup', SignUp.as_view()), #Create account
	url(r'^signin', SignIn.as_view()), #Login
)
