from django.urls import path
from .views import home_page, Login, RegisterUser, Logout

urlpatterns = [
    path("", home_page, name="home_page"),
    path("login/", Login.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("logout/", Logout.as_view(), name="logout"),
]