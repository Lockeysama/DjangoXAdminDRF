"""DjangoXAdminDRF URL Configuration

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
from django.urls import include, path
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.routers import DefaultRouter

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls

from apps.test_app.views import FriendViewSet

from common.welcome import welcome

router = DefaultRouter()
router.register(r'friend', FriendViewSet, base_name='friend')


urlpatterns = [
    path('', welcome),
    path(
        "docs/",
        include_docs_urls(
            title='Affective Cloud API Docs',
            authentication_classes=[SessionAuthentication],
            permission_classes=[IsAuthenticated],
        ),
    ),
    url(r'^(?P<version>[v1]+)/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^admin/', admin.site.urls),
]
