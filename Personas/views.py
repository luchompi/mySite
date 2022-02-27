from django.views.generic import CreateView,DetailView,UpdateView
from django.views.generic.edit import DeleteView
from .models import Cliente,Autor
from .forms import clienteForm,autorForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class ClienteCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url='/auth/login'
    permission_required='Personas.add_cliente'
    model = Cliente
    form = clienteForm
    fields =[
        'iden',
        'nombre',
        'apellidos',
        'direccion',
        'correo',
    ]
    template_name = "Personas/clientes.html"
    success_url = "."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if consulta := self.request.GET.get('identificacion'):
            context["query"] = Cliente.objects.filter(iden__icontains=consulta)
        else:
            context["query"] = Cliente.objects.all()
        return context

class ClienteUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url='/auth/login'
    permission_required=['Personas.view_cliente','Personas.change_cliente']
    model = Cliente
    form = clienteForm
    fields =[
        'iden',
        'nombre',
        'apellidos',
        'direccion',
        'correo',
    ]
    success_url = "/personas/clientes/actualizar/{iden}"
    model = Cliente
    template_name = "Personas/update.html"

class ClienteDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url='/auth/login'
    permission_required='Personas.delete_cliente'
    model = Cliente
    template_name = "Personas/delete.html"
    success_url = "/personas/clientes/"
