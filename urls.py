from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^about$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html')),

    url(r'^admin/', include(admin.site.urls)),
)
