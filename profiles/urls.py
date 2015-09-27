from django.conf.urls import patterns, url

from profiles import views

urlpatterns = patterns('',
  url(r'^$', views.profiles_list, name='profiles_list'),
  url(r'^new$', views.profiles_create, name='profiles_new'),
  url(r'^edit/(?P<pk>\d+)$', views.profiles_update, name='profiles_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.profiles_delete, name='profiles_delete'),
)