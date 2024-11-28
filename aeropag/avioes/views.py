from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Aviao
from .forms import AviaoForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

def lista_avioes(request):
    
    avioes = Aviao.objects.filter(usuario=request.user) 
    return render(request, 'lista_avioes.html', {'object_list': avioes})



def editar_aviao(request, pk):
    aviao = get_object_or_404(Aviao, pk=pk)
    if request.method == 'POST':
        form = AviaoForm(request.POST, instance=aviao)
        if form.is_valid():
            form.save()
            return redirect('listar-avioes')  # Substitua pelo nome correto da URL de lista
    else:
        form = AviaoForm(instance=aviao)
    return render(request, 'editar_aviao.html', {'form': form})


def excluir_aviao(request, pk):  # Corrigido: hífen substituído por sublinhado
    if request.method == 'POST':
        aviao = get_object_or_404(Aviao, pk=pk)
        aviao.delete()
        messages.success(request, "Avião excluído com sucesso!")
        return redirect('listar-avioes')  # Substitua pelo nome correto da URL de lista
    return redirect('listar-avioes')  # Em caso de GET, redireciona sem excluir



class AviaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Aviao
    form_class = AviaoForm
    template_name = 'forma.html'
    success_url = reverse_lazy('listar-avioes')

    def form_valid(self, form):
        form.instance.usuario = self.request.user 
        return super().form_valid(form)


class AviaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Aviao
    form_class = AviaoForm
    template_name = 'forma.html'
    success_url = reverse_lazy('listar-avioes')

    def get_object(self, queryset=None):
        return get_object_or_404(Aviao, pk=self.kwargs['pk'], usuario=self.request.user) 


class AviaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Aviao
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-avioes')

    def get_object(self, queryset=None):
        return get_object_or_404(Aviao, pk=self.kwargs['pk'], usuario=self.request.user)  

class AviaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Aviao
    template_name = 'listas/aviao.html'

    def get_queryset(self):
        return Aviao.objects.filter(usuario=self.request.user)  



def get_avioes(request):
    avioes = Aviao.objects.filter(usuario=request.user).values('prefixo', 'grupo', 'toneladas') 
    return JsonResponse({'avioes': list(avioes)})

