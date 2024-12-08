from django.contrib.auth import views as django_auth_views
from django.urls import path

app_name = "users"

urlpatterns = [
    path("login/", django_auth_views.LoginView.as_view(), name="login"),
]
