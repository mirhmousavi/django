"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from socket import gethostbyname
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.set('test', 'test')


def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def test_get_redis(request):
    result = r.get('test')
    return HttpResponse(result)


def test_get_hostname(request):
    result = gethostbyname('surlfy.com')
    return HttpResponse(result)


urlpatterns = [
    path('test/', test),
    path('test_get_redis/', test_get_redis),
    path('test_get_hostname/', test_get_hostname),
    path('admin/', admin.site.urls),
]
