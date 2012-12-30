# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from django.http import Http404
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from todolistapp.models import Category
from todolistapp.models import Task
from todolistapp.forms import TaskForm
from todolistapp.forms import TaskEditForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import defaultfilters
from django.utils import timezone
# Create your views here.


def home(request):
    if not request.user.is_authenticated():
        return TemplateResponse(request, 'todolist/home.html',)
    else:
        return TemplateResponse(request, 'todolist/homeuser.html',)


@login_required
def list(request):
    if "mensaje" in request.session:
        mensaje = request.session["mensaje"]
        del request.session["mensaje"]
    else:
        mensaje = ""
    try:
        usuario = request.user
        tasks = Task.objects.filter(owner=usuario).order_by('id')
    except Task.DoesNotExist:
            return render_to_response('todolist/list.html', {'task': tasks,
                "mensaje": mensaje}, context_instance=RequestContext(request))
    return render_to_response('todolist/list.html', {'task': tasks,
        "mensaje": mensaje}, context_instance=RequestContext(request))


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


@login_required
def delete_task(request, task_id):
    """View para borrar una tarea, por id."""
    task = Task.objects.get(id=task_id)
    task.delete()
    request.session["mensaje"] = """La tarea con id """ + task_id + """ ha
                                   sido borrada exitosamente"""
    return redirect("list")


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Se procesan los datos de form.cleaned_data
            #form.cleaned_data['title']
            task = form.save(commit=False)
            task.slug = defaultfilters.slugify(task.title)
            task.state = u'P'
            task.completed_date = None
            task.creation_date = timezone.now()
            task.owner = request.user
            task.save()

#            myslug = text.slugify(form.cleaned_data['title'])
#            mystate = u'P'
#            mycreation_date = timezone.now()
#            mycompleted_date = None
#            myowner = request.user
#            tarea = Task(slug=myslug,
#                        state=mystate,
#                        creation_date=mycreation_date,
#                        completed_date=mycompleted_date,
#                        owner=myowner)
#            form = TaskForm(request.POST, instance=tarea)
#            form.save()  # task = form.save()
            return HttpResponseRedirect(reverse('list'))
    else:
        form = TaskForm()
    return TemplateResponse(request,
             'todolist/create_task.html', {'form': form, })


def edit_task(request, task_id):
    """Vista para editar una tarea, por id."""
    tarea = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskEditForm(request.POST, instance=tarea)
#        form = TaskEditForm(request.POST)
        if form.is_valid():

           # task = Task.objects.get(id=task_id)
           # form = TaskEditForm(request.POST, instance=task)
            request.session["mensaje"] = "La tarea con id " + task_id + """ ha
            sido editada exitosamente"""
            form.save()
            return HttpResponseRedirect(reverse('list'))
    else:
        form = TaskEditForm(instance=tarea)
    return TemplateResponse(request,
             'todolist/edit_task.html', {'form': form, })


@login_required
def filter_category(request, category_id):
    if "mensaje" in request.session:
        mensaje = request.session["mensaje"]
        del request.session["mensaje"]
    else:
        mensaje = ""
    try:
        usuario = request.user
        categoria = Category.objects.filter(id=category_id)
        tasks = Task.objects.filter(owner=usuario,
            category=categoria).order_by('id')
    except Task.DoesNotExist:
            return render_to_response('todolist/list.html', {'task': tasks,
                "mensaje": mensaje}, context_instance=RequestContext(request))
    return render_to_response('todolist/list.html', {'task': tasks,
        "mensaje": mensaje}, context_instance=RequestContext(request))


@login_required
def order_by_limit_date_asc(request):
    if "mensaje" in request.session:
        mensaje = request.session["mensaje"]
        del request.session["mensaje"]
    else:
        mensaje = ""
    try:
        usuario = request.user
        tasks = Task.objects.filter(owner=usuario).order_by('limit_date')
    except Task.DoesNotExist:
            return render_to_response('todolist/list.html', {'task': tasks,
                "mensaje": mensaje}, context_instance=RequestContext(request))
    return render_to_response('todolist/list.html', {'task': tasks,
        "mensaje": mensaje}, context_instance=RequestContext(request))


@login_required
def order_by_limit_date_desc(request):
    if "mensaje" in request.session:
        mensaje = request.session["mensaje"]
        del request.session["mensaje"]
    else:
        mensaje = ""
    try:
        usuario = request.user
        tasks = Task.objects.filter(owner=usuario).order_by('-limit_date')
    except Task.DoesNotExist:
            return render_to_response('todolist/list.html', {'task': tasks,
                "mensaje": mensaje}, context_instance=RequestContext(request))
    return render_to_response('todolist/list.html', {'task': tasks,
        "mensaje": mensaje}, context_instance=RequestContext(request))
