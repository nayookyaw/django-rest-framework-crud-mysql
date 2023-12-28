from django.urls import URLPattern, path
from . import views

urlpatterns: list[URLPattern] = [
    path(route='<int:pk>', view=views.RoleView().as_view(), name="role_add_update_delete"),
    path(route='list', view=views.RoleListView().as_view(), name="role_list")
]
