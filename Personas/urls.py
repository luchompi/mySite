from django.urls import path
from . import views as v

app_name="personas"

urlpatterns = [
    path('clientes/',v.ClienteCreateView.as_view(),name="clienteIndex"),
    path('clientes/actualizar/<pk>',v.ClienteUpdateView.as_view(),name="clienteActualizar"),
    path('clientes/eliminar/<pk>',v.ClienteDeleteView.as_view(),name="clienteBorrar"),
]
