#coding:utf-8
from django.conf.urls import url
from django_web import views

urlpatterns = [
    url(r'^blog/$',views.blog,name='blog'),
    url(r'^blog/columns/$',views.blog,name='columns'),
    url(r'^blog/blogsingle/$',views.blogViws,name='blogVise'),
    url(r'^index/$',views.index,name='indexs'),
    url(r'^$',views.index,name='index')

]
