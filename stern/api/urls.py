from django.urls import path
from . import views
from .rpc import rpc_methods

urlpatterns = [
    path('', views.index, name='index'),
    path('ping', views.Pinger.as_view(), name='pinger'),
    path('rpc/train', rpc_methods.train, name="rpc"),
]
