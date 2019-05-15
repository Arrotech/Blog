from django.conf.urls import url, include
from myblog.views import home

urlpatterns = [
    url(r'^$', home),
]