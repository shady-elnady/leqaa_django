from django.urls import path

from .views import login_view, logout_view, home_view, find_user_view


app_name = "Logs"


urlpatterns = [
    path("", home_view, name="Home"),
    path("login/", login_view, name="LogIn"),
    path("logout/", logout_view, name="LogOut"),
    path("classify/", find_user_view, name="Classify"),
]
