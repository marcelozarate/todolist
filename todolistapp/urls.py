# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
# from django.conf.urls import patterns, include, url


urlpatterns = patterns('todolistapp.views',
#    url(r'^testing/$', 'testing'),
    url(r'^task/(?P<task_id>\d+)/$', 'task_detail', name='task-detail'),
    url(r'^delete-task/(?P<task_id>\d+)/$', 'delete_task', name='delete-task'),
    url(r'^create-task/$', 'create_task', name='create-task'),
    url(r'^edit-task/(?P<task_id>\d+)/$', 'edit_task', name='edit-task'),
    url(r'^filter-category/(?P<category_id>\d+)/$', 'filter_category',
        name='filter-category'),
    url(r'^$', 'list', name='list'),
    url(r'^ord-l-date-asc/$', 'order_by_limit_date_asc',
        name='order-by-limit-date-asc'),
    url(r'^ord-l-date-desc/$', 'order_by_limit_date_desc',
        name='order-by-limit-date-desc'),
)
