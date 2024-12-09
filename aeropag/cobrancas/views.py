from django.shortcuts import render, get_object_or_404, redirect
from .models import Cobranca
from .forms import CobrancaForm
from django.core.exceptions import ValidationError

# Função para listar as cobranças
def CobrancaList(request):
    cobrancas = Cobranca.objects.all()
    return render(request, 'cobranca/listar.html', {'cobrancas': cobrancas})

def CobrancaCreate(request):
    if request.method == 'POST':
        form = CobrancaForm(request.POST)
        if form.is_valid():
            try:
                cobranca = form.save(commit=False)
                cobranca.save()  # O cálculo do valor total ocorre no método save do modelo
                return redirect('listar_cobrancas')
            except Exception as e:
                form.add_error(None, f"Erro ao salvar a cobrança: {str(e)}")
    else:
        form = CobrancaForm(user=request.user)
    return render(request, 'form_cobranca.html', {'form': form})


# Função para atualizar uma cobrança existente
def CobrancaUpdate(request, id):
    cobranca = get_object_or_404(Cobranca, id=id)
    if request.method == 'POST':
        form = CobrancaForm(request.POST, instance=cobranca)
        if form.is_valid():
            try:
                form.save()
                return redirect('listar_cobrancas')
            except Exception as e:
                form.add_error(None, f"Erro ao atualizar a cobrança: {str(e)}")
    else:
        form = CobrancaForm(instance=cobranca)
    return render(request, 'templates/form.html', {'form': form})

# Função para excluir uma cobrança
def CobrancaDelete(request, id):
    cobranca = get_object_or_404(Cobranca, id=id)
    if request.method == 'POST':
        cobranca.delete()
        return redirect('listar_cobrancas')
    return render(request, 'templates/confirmar_exclusão.html', {'cobranca': cobranca})

# Função para ver os detalhes de uma cobrança
def CobrancaDetails(request, id):
    cobranca = get_object_or_404(Cobranca, id=id)
    return render(request, 'detalhes.html', {'cobranca': cobranca})
