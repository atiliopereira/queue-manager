from datetime import datetime

from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from dissoi.forms import LoginForm
from dissoi.models import Sesion
from funcionario.models import Funcionario
from turno.constants import EstadoBox
from turno.models import Box
import datetime

def logout_user(request):
    user_id = request.GET.get('id_usuario','')
    user = User.objects.get(pk=user_id) if user_id else request.user

    if user.is_authenticated():
        box = Box.objects.filter(funcionario__usuario=user)
        if box.exists():
            box = box.first()
            box.funcionario = None
            box.estado = EstadoBox.INHABILITADO
            box.save()

    sesiones = Sesion.objects.filter(funcionario__usuario=request.user, hora_logout__isnull=True)
    if sesiones.exists():
        sesion = sesiones.first()
        sesion.hora_logout = datetime.datetime.now()
        sesion.save()

    return HttpResponseRedirect(reverse('dissoi_login'))

def login_user(request):

    def login_response(form):
        return render_to_response('admin/login.html',
                           {'form': form},
                           context_instance=RequestContext(request))
    logout(request)
    if request.POST:
        form = LoginForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']

        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active and user.is_staff:
                    funcionario = Funcionario.objects.filter(usuario__username=username)
                    if not funcionario.exists() and not user.is_superuser:
                        messages.error(request, 'Este usuario no tiene un funcionario asociado!')
                        return login_response(form)

                    id_box = request.POST.get('box','')
                    if id_box:
                        box = Box.objects.get(pk=id_box)
                        box.estado = EstadoBox.LIBRE
                        box.funcionario = funcionario.first()
                        box.save()

                    login(request, user)

                    if not Sesion.objects.filter(funcionario=funcionario, hora_logout__isnull=True).exists() and not user.is_superuser:
                        # messages.warning(request, 'Este usuario ya se encuentra logueado!')
                        # return login_response(form)
                        Sesion.objects.create(funcionario=funcionario.first())

                    url = '/admin/'
                    sitio = request.POST['sitio']
                    if sitio == 'B':
                        url = '/turno/box_atencion'
                    if sitio == 'T':
                        url = '/admin/turno/ticket/add/'
                    return HttpResponseRedirect(url)
    else:
        form = LoginForm()
    return login_response(form)