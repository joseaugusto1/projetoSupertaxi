from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
   url(r'^$', 'corridas.views.index'),
   url(r'^validar/$', 'corridas.views.validar'), 
)
