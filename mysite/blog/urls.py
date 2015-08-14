from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^page-with-links/$', views.page_with_links, name='page_with_links'),
]