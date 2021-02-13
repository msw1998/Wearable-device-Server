from django.urls import path
from . import views

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.login_request, name="login"),
    path("register",views.register,name="register"),
]
