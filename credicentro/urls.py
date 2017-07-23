from django.conf.urls import include, url

from django.contrib import admin
from django.contrib.auth.decorators import login_required

from django.contrib import admin


from dissoi.sites import dissoi_site
from dissoi.views import login_user

admin.autodiscover()
admin.site.site_header = 'CrediCentro'

admin.site.login = login_user

urlpatterns = [
    # Examples:
    # url(r'^$', 'credicentro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/login/', login_user),
    url(r'^turno/', include('turno.urls')),
    url(r'^dissoi/', include('dissoi.urls')),
    url(r'^cliente/', include('cliente.urls'))
]

