from typing import Any, Dict
from django.views.generic import TemplateView
from .models import Funcionario, Servico, Recurso, Cliente

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['recursos'] = Recurso.objects.all()
        context['clientes'] = Cliente.objects.order_by('?').all()
        return context
