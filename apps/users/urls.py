from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^signup/$', 'apps.users.views.userregister', name="register"), #Create account
	url(r'^signin/$', 'apps.users.views.userlogin', name="login"), #Login
    url(r'^logout/$', 'apps.users.views.LogOut', name = "logout"),
)
