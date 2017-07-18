
from dal import autocomplete

from cliente.models import Cliente
from django.db.models import Q


class ClienteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Cliente.objects.none()

        qs = Cliente.objects.filter(activo=True)
        if self.q:
            qs = qs.filter(Q(nombre__istartswith=self.q) | Q(apellido__istartswith=self.q) |
                           Q(documento__icontains=self.q))
        return qs