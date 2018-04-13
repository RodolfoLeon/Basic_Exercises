from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^additem$', views.additem),
    url(r'^createitem$', views.createitem),
    url(r'^logout$', views.logout),
    url(r'^wishitem/(?P<id>\d+)$', views.iteminfo),
]