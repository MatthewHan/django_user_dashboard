__author__ = 'MatthewHan'
from django.conf.urls import patterns, url # import functions to match patterns
from apps.home import views
urlpatterns = [
    url(r'^$', views.index, name = 'home'),
]