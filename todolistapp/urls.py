# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
# from jango.conf.urls import patterns, include, url


urlpatterns = patterns('todolistapp.views',
#    url(r'^testing/$', 'testing'),
    url(r'^task/(?P<task_id>\d+)/$', 'task_detail', name='task-detail'),
    url(r'^delete-task/(?P<task_id>\d+)/$', 'delete_task', name='delete-task'),
#    url(r'^new-task/$', 'new_task', name='new-task'),
    url(r'^$', 'list', name='list'),
)
