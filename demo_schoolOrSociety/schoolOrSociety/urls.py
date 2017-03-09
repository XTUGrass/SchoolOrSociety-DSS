from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from schoolOrSociety.views import index, questionary, result, process

urlpatterns = [
    url(r'^questionary', views.questionary, {'template_name': 'schoolOrSociety/questionary.html'}, name='questionary'),
    url(r'^result', views.result, name='result'),
    url(r'^process', views.process, name='process'),
    url(r'^index', views.index, {'template_name': 'schoolOrSociety/index.html'}, name='index'),
    url(r'^.?', views.index, {'template_name': 'schoolOrSociety/index.html'}, name='index'),
]