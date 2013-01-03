# -*- coding: utf-8 *-*
from todolistapp.models import Task
from todolistapp.models import Category
from django.forms import ModelForm
from django.forms import widgets
#from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        widgets = {
                    'limit_date': widgets.SplitDateTimeWidget(),
                  }
        exclude = ('slug',
                    'state',
                    'creation_date',
                    'completed_date',
                    'owner',)


class TaskEditForm(ModelForm):
    class Meta:
        model = Task
        widgets = {
                    'limit_date': widgets.SplitDateTimeWidget(),
                    'completed_date': widgets.SplitDateTimeWidget(),
                  }
        exclude = ('slug',
                    'creation_date',
                    'owner',)


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = ('slug', 'owner',)
