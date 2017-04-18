
from dal import autocomplete

from turno.constants import EstadoBox
from turno.models import Box


class BoxInhabilitadoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Box.objects.none()

        qs = Box.objects.filter(estado=EstadoBox.INHABILITADO,activo=True)

        if self.q:
            qs = qs.filter(nombre__istartswith=self.q)
        return qs

