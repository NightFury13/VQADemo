from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^add_page/(?P<category_name>[\w\-]+)/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name>[\w\-]+)/$', views.category, name='category'),
    url(r'^like_category/$', views.like_category, name='like_category'),
)
