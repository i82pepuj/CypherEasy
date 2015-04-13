from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import password_reset, password_reset_done, password_change, password_change_done
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	(r'^accounts/', include('registration.backends.simple.urls')),
    #(r'^profiles/', include('profiles.urls')),
    (r'^$', TemplateView.as_view(template_name='main.html')),
    (r'^cifrados/$', TemplateView.as_view(template_name='cifrados.html')),
    (r'^cesar/$', TemplateView.as_view(template_name='cesar.html')),
    (r'^afin/$', TemplateView.as_view(template_name='afin.html')),
    (r'^mochila/$', TemplateView.as_view(template_name='mochila.html')),
    (r'^rsa/$', TemplateView.as_view(template_name='rsa.html')),
    (r'^firma/$', TemplateView.as_view(template_name='firma.html')),
    (r'^sobrenosotros/$', TemplateView.as_view(template_name='sobrenosotros.html')),
    (r'^contacto/$', TemplateView.as_view(template_name='contacto.html')),
    (r'^criptografia/$', TemplateView.as_view(template_name='criptografia.html')),
    url(r'^cifrarcesar/$', 'forms.views.cifrar_Cesar'),
    url(r'^descifrarcesar/$', 'forms.views.descifrar_Cesar'),
    url(r'^cifrarafin/$', 'forms.views.cifrar_Afin'),
    url(r'^descifrarafin/$', 'forms.views.descifrar_Afin'),
    url(r'^cifrarmochila/$', 'forms.views.cifrar_Mochila'),
    url(r'^descifrarmochila/$', 'forms.views.descifrar_Mochila'),
    url(r'^generarclavemochila/$', 'forms.views.generar_Clave_Mochila'),
    url(r'^introducirclavemochila/$', 'forms.views.introducir_Clave_Mochila'),
    url(r'^cifrarrsa/$', 'forms.views.cifrar_RSA'),
    url(r'^descifrarrsa/$', 'forms.views.descifrar_RSA'),
    url(r'^generarclaversa/$', 'forms.views.generar_Clave_RSA'),
    url(r'^introducirclaversa/$', 'forms.views.introducir_Clave_RSA'),
    url(r'^enviarcorreo/$', 'forms.views.correoFirma')

)

urlpatterns += patterns('',
    (r'^accounts/password_reset/$', password_reset, {'template_name': 'registration/password_reset.html'}),
    (r'^accounts/password_reset_done/$', password_reset_done, {'template_name': 'registration/password_reset_done.html'}),
    (r'^accounts/password_change/$', password_change, {'template_name': 'registration/password_change.html'}),
    (r'^accounts/password_change_done/$', password_change_done, {'template_name': 'registration/password_change_done.html'}),
)

if settings.DEBUG and settings.STATIC_ROOT:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'),
            'django.views.static.serve',
            {'document_root' : settings.STATIC_ROOT }),)
