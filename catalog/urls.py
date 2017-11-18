from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.box_list, name='box_list'),
    url(r'^get_pass/(?P<pk>\d+)/$', views.get_pass, name='get_pass'),
    url(r'^return_pass/(?P<pk>\d+)/$', views.return_pass, name='return_pass'),
    url(r'^search_form/$', views.search_form, name='search_form'),
    url(r'^search/$', views.search, name='search'),
]