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


def index(request):
    list_items = ""
    pages = list(pages_challenges.keys())

    for page in pages:
        capitalized_page = page.capitalize()
        page_path = reverse("abdullah-test", args=[page])
        list_items += f"<li><a href=\"{page_path}\">{capitalized_page}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def pagesByNumbers(request, page):
    pages = list(pages_challenges.keys())

    if page > len(pages):
        return HttpResponseNotFound("<h1>Error not supported by abdullah!</h2>")

    redirect_page = pages[page - 1]
    redirect_path = reverse("abdullah-test", args=[redirect_page])
    return HttpResponseRedirect(redirect_path)


def page(request, page):
    try:
        pages_user = pages_challenges[page]
        data_display = f"<h1><br>{pages_user}</h2>"
        return HttpResponse(data_display)
    except:
        return HttpResponseNotFound("<h1>Error not supported by abdullah!</h2>")
