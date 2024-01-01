"""
URL configuration for watermeterbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from typing import Any
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

# swagger import
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings

schema_view : Any= get_schema_view(
    info=openapi.Info(
        title="Swagger Doc",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(route='admin/', view=admin.site.urls),
    path(route='role/', view=include(arg='src.role.urls')),
    path(route='user/', view=include(arg='src.user.urls')),

    path(route='swagger/', view=schema_view.with_ui(renderer='swagger', cache_timeout=0),name='schema-swagger-ui'),
    path(route='docs/', view=include_docs_urls(title='Your API Documentation')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
