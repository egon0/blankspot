from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from node_registration import views

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
	url(r'^todo$', TemplateView.as_view(template_name="todo.html"), name='todo'),
	url(r'^about/', TemplateView.as_view(template_name="about.html"), name='about'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'position', include('node_registration.urls')),
)

