from django.contrib.auth import views as django_auth_views
from django.urls import path, reverse_lazy

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
    path(
        "password/change/",
        django_auth_views.PasswordChangeView.as_view(
            template_name="users/password_change.html",
            success_url=reverse_lazy("users:password_change_done"),
        ),
        name="password_change",
    ),
    path(
        "password/change/done",
        django_auth_views.PasswordChangeDoneView.as_view(
            template_name="users/password_change_done.html"
        ),
        name="password_change_done",
    ),
]
