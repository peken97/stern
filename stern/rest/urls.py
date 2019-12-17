from django.urls import path
from modernrpc.views import RPCEntryPoint

from . import views, rpc_methods

urlpatterns = [
    path('', views.index, name='index'),
    path('ping', views.Pinger.as_view(), name='pinger'),
    path('rpc', rpc_methods.rpc_request_handler, name="rpc"),
]
