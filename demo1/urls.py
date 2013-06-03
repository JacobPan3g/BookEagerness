from django.conf.urls import patterns, include, url
from demo1 import settings
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
        settings.STATIC_PATH}),
    url(r'^$', views.index),
    url(r'^result/', views.result),
    url(r'^logout/', views.logout),
    # Examples:
    # url(r'^$', 'demo1.views.home', name='home'),
    # url(r'^demo1/', include('demo1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
