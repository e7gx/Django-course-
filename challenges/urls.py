from django.urls import path
from . import views

urlpatterns = [
    path("<int:page>", views.pagesByNumbers),
    path("<str:page>", views.page, name="abdullah-test"),
]
