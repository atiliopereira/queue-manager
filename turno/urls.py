from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from turno.ajax import get_tickets, box_atencion_ajax
from turno.autocomplete import BoxInhabilitadoAutocomplete
from turno.views import ColaClienteSideTemplateView, BoxAtencionTemplateView, \
    BoxListaTicketsView

urlpatterns = [
    # Examples:
    # url(r'^$', 'queue.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^colacliente/', ColaClienteSideTemplateView.as_view(), name='cola_cliente'),
    url(r'^box_atencion/(?P<ticket_id>\d+)/$', login_required(BoxAtencionTemplateView.as_view()), name='box_atencion'),
    url(r'^box_tickets_list/', login_required(BoxListaTicketsView.as_view()), name='box_tickets_list'),
    url(r'^turno/api/get_tickets', get_tickets, name='turno_get_tickets'),
    url(r'^turno/api/box_atencion_ajax', box_atencion_ajax, name='box_atencion_ajax'),
    url(
        r'^box_inhabilitado-autocomplete/$',
        BoxInhabilitadoAutocomplete.as_view(),
        name='box_inhabilitado-autocomplete',
    ),
]