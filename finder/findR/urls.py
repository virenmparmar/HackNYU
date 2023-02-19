from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "findR"
urlpatterns = [
    path("", views.index, name="index"),
    path(
        "login",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    path(
        "logout",
        auth_views.LogoutView.as_view(template_name="base.html"),
        name="logout",
    ),
    path("register", views.register, name="register"),
    path("add_listing", views.add_listing, name="add_listing"),
    path("browse", views.browse, name="browse")

]
