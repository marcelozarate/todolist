# -*- coding: utf-8 *-*
from todolistapp.models import Task
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

#class TaskForm(forms.Form):
#    title = forms.CharField(max_length=128)
#    slug = forms.
#    description =
#    state =
#    creation_date =
#    limit_date =
#    completed_date =
#    category =
#    owner =
