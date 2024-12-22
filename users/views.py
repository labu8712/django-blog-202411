import datetime

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import TemplateView


class CBView(TemplateView):
    template_name = "users/cbv.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "hello world"
        return context


def set_cookie(request):
    data = request.GET.get("data", "empty")

    now = timezone.now()  # UTC
    expires = now + datetime.timedelta(minutes=1)

    response = HttpResponse("OKOK")
    response.set_cookie("data", data, expires=expires)
    return response


def show_cookie(request):
    return HttpResponse(request.COOKIES.get("data"))


def delete_cookie(request):
    response = HttpResponse("Done")
    response.delete_cookie("data")
    return response


def set_session(request):
    data = request.GET.get("data", "empty")
    request.session["data"] = data
    return HttpResponse("okok")


def show_session(request):
    return HttpResponse(request.session.get("data"))


def delete_session(request):
    if "data" in request.session:
        del request.session["data"]

    return HttpResponse("Done")


def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("users:login")

    return render(request, "users/register.html", {"form": form})
