from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
pages_challenges = {

    "abdullah": "my first name",
    "ibrahim": "my second name",
    "mo":None,
    "gh": "my last name"
}


def index(request):
    pages = list(pages_challenges.keys())

    return render(request,"challenges/index.html",{
        "pages": pages
    })


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
        pages_title = pages_challenges[page]
        
        return render(request, "challenges/challenge.html", {
            "text": pages_user,
            "title": pages_title,
            "name": page.capitalize(),
        })

    except:
        return HttpResponseNotFound("<h1>Error not supported by abdullah!</h2>")
