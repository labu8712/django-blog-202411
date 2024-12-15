"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from users import views as user_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("users/", include("users.urls")),
    path("set-cookie/", user_views.set_cookie, name="set_cookie"),
    path("show-cookie/", user_views.show_cookie, name="show_cookie"),
    path("delete-cookie/", user_views.delete_cookie, name="delete_cookie"),
    path("set-session/", user_views.set_session, name="set_session"),
    path("show-session/", user_views.show_session, name="show_session"),
    path("delete-session/", user_views.delete_session, name="delete_session"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
