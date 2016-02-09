from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^stream/$', 'apps.stream.views.stream', name="stream"), #Stream audio page
)
