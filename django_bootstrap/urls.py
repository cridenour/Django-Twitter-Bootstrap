from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^about$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
