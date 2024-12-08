from django.contrib.auth import views as django_auth_views
from django.urls import path

from users import views as user_views

app_name = "users"

urlpatterns = [
    path(
        "login/",
        django_auth_views.LoginView.as_view(
            template_name="users/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("logout/", django_auth_views.LogoutView.as_view(), name="logout"),
    path("register/", user_views.register, name="register"),
]
