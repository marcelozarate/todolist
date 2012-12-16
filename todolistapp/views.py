# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
#from django.http import HttpResponseRedirect
#from django.http import Http404
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from todolistapp.models import Task
#from todolistapp.forms import TaskForm
#from django.core.urlresolvers import reverse

# Create your views here.


def home(request):
    if not request.user.is_authenticated():
        return TemplateResponse(request, 'todolist/home.html',)
    else:
        return TemplateResponse(request, 'todolist/homeuser.html',)


@login_required
def list(request):
    try:
        usuario = request.user
        tasks = Task.objects.filter(owner=usuario).order_by('id')
    except Task.DoesNotExist:
        return TemplateResponse(request,
                 'todolist/list.html', {'task': tasks, })
    return TemplateResponse(request, 'todolist/list.html', {'task': tasks, })


@login_required
def task_detail(request, task_id):
    """View para mostrar el detalle de un task particular, por id."""
    task = get_object_or_404(Task, id=task_id)
    # este código comentado es equivalente a la línea de arriba
    #try:
        #post = Post.objects.get(id=post_id)
    #except Post.DoesNotExist:
        #return HttpResponse('No existe!')
    return TemplateResponse(request,
        'todolist/task_detail.html', {'task': task})
