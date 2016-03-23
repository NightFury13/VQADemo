from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^compute_vqa/$', views.compute_vqa, name='compute_vqa'),
]
