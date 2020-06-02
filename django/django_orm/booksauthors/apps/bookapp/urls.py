from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^processauthor/(?P<x>\d+)$', views.processauthor),
    url(r'^processbook/(?P<y>\d+)$', views.processbook),
    url(r'^authors/(?P<y>\d+)$', views.displayauthor),
    url(r'^(?P<x>\d+)$', views.displaybook),
    url(r'^addauthor$', views.addauthor),
    url(r'^authors$', views.authors),
    url(r'^addbook$', views.addbook),
    url(r'^$', views.index),
    ]