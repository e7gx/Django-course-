from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.


def step1(request):
    return HttpResponse('hi 1 ,  you can know switch between pages')


def step2(request):
    return HttpResponse('hi 2')


def step3(request):
    return HttpResponse('hi 3 ,  you can know switch between pages')


def step4(request):
    return HttpResponse('hi 4')



def pages(request,pages):
    pages_user = None
    if pages == "abdullah":
        pages_user = "ارحب مليون"
    elif pages == "ibrahim":    
          pages_user = " 2 ي هلا ومرحبا"
    elif pages == "mo":    
          pages_user = "3 ي هلا ومرحبا"
    elif pages == "gh":    
          pages_user = "4 ي هلا ومرحبا"
    else :
         return HttpResponseNotFound('الخلا')
    return HttpResponse(pages_user)