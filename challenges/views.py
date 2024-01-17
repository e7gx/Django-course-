from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
pages_challenges = {

    "abdullah": "my first name",
    "ibrahim": "my second name",
    "mo": "my theard name",
    "gh": "my last name"
}


def pagesByNumbers(request, page):
    pages = list(pages_challenges.keys())

    if page > len(pages):
        return HttpResponseNotFound("<h1>Error not supported by abdullah!</h2>")

    redirect_page = pages[page - 1]
    redirect_path = reverse("abdullah-test",args=[redirect_page])
    return HttpResponseRedirect(redirect_path)


def page(request, page):
    try:
        pages_user = pages_challenges[page]
        data_display = f"<h1><br>{pages_user}</h2>"
        return HttpResponse(data_display)
    except:
        return HttpResponseNotFound("<h1>Error not supported by abdullah!</h2>")
