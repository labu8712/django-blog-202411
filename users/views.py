import datetime

from django.http import HttpResponse
from django.utils import timezone


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
