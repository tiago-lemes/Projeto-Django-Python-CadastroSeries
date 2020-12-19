from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect
from . import forms
from . import models

def cadastro(request):
    form = forms.GeneroForm()
    print('Vou salvar os dados...request')
    if request.method == 'POST':
        print('Vou salvar os dados...')
        form = forms.GeneroForm(request.POST)
        print(form)

        if form.is_valid():
            form.save(commit=True)
        else:
            print('ERRO!!!')
        

    lista_genero = models.Genero.objects.order_by('id')

    data_dict = {'form': form, 'lista_dados': lista_genero}
    return render(request, 'genero/genero.html', data_dict)

def delete(request, id):
    print('Vou deletar os dados...delete')
    try:
        models.Genero.objects.filter(id=id).delete()
        form = forms.GeneroForm(request.POST)
        lista_genero = models.Genero.objects.order_by('id')

        data_dict = {'form': form, 'lista_dados': lista_genero}
        return render(request, 'genero/genero.html', data_dict)
    except:
        return HttpResponseNotAllowed()
        
def update(request, id):
    print('Vou alterar os dados...update')
    item = models.Genero.objects.get(id=id)

    if request.method == 'GET':
        form = forms.GeneroForm(initial={'descricao':item.descricao})
        data_dict = {'form': form}

        return render(request, 'genero/genero_upd.html', data_dict)
    else:
        form = forms.GeneroForm(request.POST)
        item.descricao = form.data['descricao']
        item.save()

        return redirect('../')
