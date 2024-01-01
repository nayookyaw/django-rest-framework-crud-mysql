from django.urls import URLPattern, path
from . import views

urlpatterns: list[URLPattern] = [
    path(route='login', view=views.UserLogin.as_view(), name="user_login"),

    path(route='<int:pk>', view=views.UserView.as_view(), name="user_save_update_delete")
]