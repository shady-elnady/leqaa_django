from django.urls import path

from . import views


app_name = "User"


urlpatterns = [
    ## Api URLs
    # path("register/", UserRegistrationView.as_view(), name="user-registration"),
    # path(
    #     "register/student/",
    #     StudentRegistrationView.as_view(),
    #     name="student-registration",
    # ),
    # path("api/fire-log-in/", views.login_view, name="login"),
    path("fire-log-in/", views.login_page, name="login_page"),  # for the html page
]


"""
  https://codevoweb.com/django-implement-2fa-two-factor-authentication/

  https://studygyaan.com/tag/django-rest-framework

"""
