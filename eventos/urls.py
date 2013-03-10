from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('festty.eventos.views',
    # Examples:
    # url(r'^$', 'festty.views.home', name='home'),
    # url(r'^festty/', include('festty.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'index', name='index'),
    url(r'^listar/(?P<ano>\d{4})/(?P<mes>\d{1,2})/(?P<dia>\d{1,2})/$', 'listar', name='listar'),
    url(r'^informacoes/(?P<slug>[-\w]+)/$', 'informacoes', name='informacoes'),
    url(r'^chamada/$', 'chamada', name='chamada'),
    url(r'^destaque/$', 'destaque', name='destaque'),
    url(r'^publique/$', 'publique', name='publique'),
)
