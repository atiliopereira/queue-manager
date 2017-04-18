from django.conf.urls import patterns, url

from dissoi.views import login_user, logout_user

urlpatterns = [
    url(r'^login/$', login_user, name ='dissoi_login'),
    url(r'^logout/$', logout_user, name='dissoi_logout'),
]