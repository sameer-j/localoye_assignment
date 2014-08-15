from django.conf.urls import patterns, url
from localoye import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))