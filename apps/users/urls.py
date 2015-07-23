__author__ = 'MatthewHan'
from django.conf.urls import patterns, url # import functions to match patterns
from apps.users.views import UsersView, Login, Register, DisplayUser, DeleteUser, UpdateUser
urlpatterns = [
    url(r'^$', UsersView.as_view()),
    url(r'^login', Login.as_view()),
    url(r'^register', Register.as_view()),
    url(r'^(?P<user_id>\d+)/', DisplayUser.as_view()),
    url(r'^(?P<user_id>\d+)/delete', DeleteUser.as_view()),
    url(r'^(?P<user_id>\d+)/edit', UpdateUser.as_view()),
]