from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from festty import settings


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^festty/', include('festty.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'festty.eventos.views.index', name='index'),
    url(r'^eventos/', include('festty.eventos.urls', namespace='eventos')),
    url(r'^calendario/', include('festty.calendario.urls', namespace='calendario')),

    # Robots.txt
    url(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt")),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT,
                            }),
    )
