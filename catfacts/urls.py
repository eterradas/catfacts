from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from apps.landing import views

urlpatterns = patterns('',
    url(r'^$', views.add_recipient),
    url(r'^thanks', views.thanks),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
