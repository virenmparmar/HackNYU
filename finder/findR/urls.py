from django.urls import path

from . import views

app_name = "findR"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("add_listing", views.add_listing, name="add_listing"),
]
