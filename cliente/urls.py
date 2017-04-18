from django.conf.urls import patterns, url

from cliente.autocomplete import ClienteAutocomplete

urlpatterns = [
    url(r'^cliente-autocomplete/$', ClienteAutocomplete.as_view(), name ='cliente-autocomplete'),
]