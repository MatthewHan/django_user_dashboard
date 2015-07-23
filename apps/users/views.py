from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import RegisterForm
class UsersView(View):
    def get(self,request):
        users = User.objects.all()
        context = {
            'users': users,
        }
        return render(request, 'users/index.html', context)
class Login(View):
    def get(self,request):
        print 'in Login View Get'
        return render(request, 'users/login.html')
    def post(self,request):
        print 'in Login View Post'
        return render(request, 'users/login.html')
class Register(View):
    def get(self,request):
        print 'in Register View Get'
        return render(request, 'users/register.html')
    def post(self,request):
        print 'in Register View Post'
        return render(request, 'users/register.html')
class DisplayUser(View):
    def get(self,request,user_id):
        print 'in DisplayUser View Get'
        return render(request, 'users/show.html')
class DeleteUser(View):
    def post(self,request,user_id):
        print 'in DeleteUser View Post'
        return render(request, 'users/index.html')
class UpdateUser(View):
    def get(self,request,user_id):
        print 'in UpdateUser View Get'
        return render(request, 'users/edit.html')
    def post(self,request,user_id):
        print 'in UpdateUser View Post'
        return render(request, 'users/edit.html')

