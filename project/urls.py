"""jun_world_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="LitMap API",
        default_version='v1',
        description="Jun World API.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="kiryanenkoav@gmail.com"),
        license=openapi.License(name="BSD License"),

    ),
    validators=['flex', 'ssv'],
    public=True,
    permission_classes=(permissions.IsAdminUser,),
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^webpush/', include('webpush.urls')),
    url(r'^api/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^', include('core.urls', 'core')),
    url(r'^api/achievement/', include('achievement.urls', 'achievement')),
    url(r'^api/places/', include('places.api_urls', 'places')),
    url(r'^places/', include('places.urls', namespace='places'))
]
