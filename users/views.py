from django.shortcuts import render
from .forms import RegisterUserForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView

def home_page(request):
    return render(request, "home/welcome.html")

class Login(LoginView):
    template_name = "accounts/login.html"


class RegisterUser(FormView):
    template_name = "accounts/register.html"
    form_class = RegisterUserForm
    success_url = "/"
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
class Logout(LogoutView):
    next_page = "/"