from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name= "index"),
    path("<int:page>", views.pagesByNumbers),
    path("<str:page>", views.page, name="abdullah-test"),
]
