from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from avioes.models import Aviao
from lembretes.models import Lembrete
from clientes.models import Cliente
from tarifas.models import Tarifa
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from datetime import datetime, timedelta

def search(request):
    query = request.GET.get('query', '')  
    
    if query:
        results = Aviao.objects.filter(nome__icontains=query)  
    else:
        results = Aviao.objects.all()  
    
    return render(request, 'search_results.html', {'query': query, 'results': results})


def dashboard(request):
    total_avioes = Aviao.objects.count()
    lista_avioes = Aviao.objects.all()
    lista_clientes = Cliente.objects.all()
    total_clientes = lista_clientes.count()
    total_tarifas = Tarifa.objects.count()
    lista_tarifas = Tarifa.objects.all()
    total_lembretes = Lembrete.objects.count()
    lista_lembretes = Lembrete.objects.all()
    
    context = {
        'total_avioes': total_avioes,
        'lista_avioes': lista_avioes,
        'total_lembretes': total_lembretes,
        'lista_lembretes': lista_lembretes,
        'lista_clientes': lista_clientes,
        'total_clientes': total_clientes,
        'total_tarifas': total_tarifas,
        'lista_tarifas': lista_tarifas,
    }
    return render(request, 'paginas/dashboard.html', context)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_avioes'] = Aviao.objects.count()
        context['lista_avioes'] = Aviao.objects.all()
        context['total_lembretes'] = Lembrete.objects.count()
        context['lista_lembretes'] = Lembrete.objects.all()
        context['lista_clientes'] = Cliente.objects.all()
        context['total_clientes'] = Cliente.objects.count()
        context['lista_tarifas'] = Tarifa.objects.all()
        context['total_tarifas'] = Tarifa.objects.count()
        return context


class IndexView(TemplateView):
    login_url = reverse_lazy('login')
    template_name = "index.html"
