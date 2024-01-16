from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
        return HttpResponseNotFound("Error not sported abdullah")

    redirect_page = pages[page - 1]
    return HttpResponseRedirect("/challenges/" + redirect_page)


def page(request, page):
    try:
        pages_user = pages_challenges[page]
        return HttpResponse(pages_user)
    except:
        return HttpResponseNotFound("Error not sported abdullah")
