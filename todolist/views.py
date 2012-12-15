# -*- coding: utf-8 *-*
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse


def register(request):
    if request.method == 'POST':  # Si ya se hizo submit del form
        form = UserCreationForm(request.POST)  # un enlace a la POST-data
        if form.is_valid(): # Si pasa la validación
#            new_user = form.save() # Se puede procesar los datos acá
            form.save()
            return HttpResponseRedirect(reverse('home'))  # Redirect
    else:
        form = UserCreationForm()  # un form sin enlazar para rellenar
    return TemplateResponse(
        request, "registration/register.html", {'form': form})
