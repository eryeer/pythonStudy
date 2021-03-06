from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^create$', views.create),
    url(r'^delete/(\d+)$', views.delete),
    url(r'^login$', views.login),
    url(r'^login_check$', views.login_check),
    url(r'^ajax_login$', views.ajax_login),
    url(r'^ajax_login_check$', views.ajax_login_check),
    url(r'^set_cookie$', views.set_cookie),
    url(r'^get_cookie$', views.get_cookie),
    url(r'^set_session$', views.set_session),
    url(r'^get_session$', views.get_session),
]
