from django.shortcuts import render

from app.forms import dadosPessoalForm, SimpleForm

def index(request):
    form = dadosPessoalForm()
    form2 = SimpleForm()
    context = {
        'form' : form,
        'form2': form2 
    }
    return render(request, 'index.html', context)
