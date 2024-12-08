from django.http import HttpResponse


def set_cookie(request):
    data = request.GET.get("data", "empty")

    response = HttpResponse("OKOK")
    response.set_cookie("data", data)
    return response


def show_cookie(request):
    return HttpResponse(request.COOKIES.get("data"))


def delete_cookie(request):
    response = HttpResponse("Done")
    response.delete_cookie("data")
    return response
