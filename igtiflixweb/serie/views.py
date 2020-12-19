# from django.shortcuts import render

# Create your views here.
# def cadastro(request):
#     return render(request, 'serie/serie.html')

#def delete(request, id):
#    return render("Hello word - Serie")

#def update(request, id):
#    return render("Hello word - Serie")


from django.shortcuts import render
from django.shortcuts import redirect

from . import forms
from . import models
from genero import models as modelsGenero


def cadastro(request):
    print("insert")
    print(request.method)
    form = forms.SerieForm()
    if request.method == 'POST':
        form = forms.SerieForm(request.POST)
        if form.is_valid():
            print("Saving")
            form.save(commit=True)
        else:
            print("ERROR")
    serie_list = models.Serie.objects.order_by('name')
    data_dict = {"serie_records": serie_list, 'form': form}

    return render(request, 'serie/serie.html', data_dict)


def delete(request, id):
    print("delete")
    models.Serie.objects.filter(id=id).delete()
    form = forms.SerieForm()
    serie_list = models.Serie.objects.order_by('name')
    data_dict = {"serie_records": serie_list, 'form': form}
    return render(request, 'serie/serie.html', data_dict)



def update(request, id):
    item = models.Serie.objects.get(id=id);
    if request.method == "GET":
        form = forms.SerieForm(initial={'name': item.name, 'idGenero': item.idGenero})
        data_dict = {'form': form}
        return render(request, 'serie/serie_upd.html', data_dict)
    else:
        form = forms.SerieForm(request.POST)
        item.name = form.data['name']
        item.idGenero = modelsGenero.Genero.objects.get(id=form.data['idGenero'])
        item.save()

        return redirect('../')



#def update(request, id):
#    item = models.Serie.objects.get(id=id)
#    print(item)
#    print('passou {0}'.format(request.method))
#    if request.method == "GET":
#        form = forms.SerieForm(initial={'name': item.name})
#        data_dict = {'form': form}
#        return render(request, 'serie/serie_upd.html', data_dict)
#    else:
#        form = forms.SerieForm(request.POST)
#        item.nome = form.data['name']
#        print(form)
#        print('-----')
#        print(item)
#        genero = modelGenero.Genero.objects.get(id=int(form.data['idGenero']))
#        print('genero>>> {0}'.format(genero))
#        item.idGenero = genero
#        item.save()
#        #serie_list = models.Serie.objects.order_by('name')
#        #data_dict = {"serie_records": serie_list, 'form': form}
#        #return render(request, 'serie/serie.html', data_dict)
#        return redirect('../')
#