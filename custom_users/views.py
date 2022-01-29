# from audioop import reverse
#
# from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.views import LoginView
# #from django.views.generic import CreateView, ListView
# from django.views.generic import CreateView
#
# from custom_users.forms import RegistrationForm
#
#
# class Registration(CreateView):
#     form_class = RegistrationForm
#     success_url = '/users/'
#     template_name = 'registration.htm'
#
# class NewLoginView(LoginView):
#     form_class = 'loginForm'
#     template_name = 'login.html'
#
#     def get_success_url(self):
#         return reverse("users:user_list")
#
#
# class UserListView(LoginView):
#     queryset = User.objects.all()
#     template_name = "user_list.html"
#
#     def get_gueryset(self):
#         return User.objects.all()
