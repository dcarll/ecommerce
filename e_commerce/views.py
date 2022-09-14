from django.shortcuts import render
from . forms import ContatoForm

def index(request):
    context = {
        "titulo": "Index",
        "conteudo": "pagina inicial"
    }
    return render(request, 'home.html', context)

def about_page(request):
    contexto = {
        "titulo": "sobre",
        "conteudo": "Sobre o ptojeto"
    }
    return render(request, 'about/about.html', contexto)

def contato(request):
    contato_form = ContatoForm(request.POST or None)
    contexto = {
        "titulo": "contato",
        "conteudo": "pagina de contato",
        "form": contato_form
    }

    if request.method == "POST":
        print(request.POST)
    if contato_form.is_valid():
        print(contato_form.cleaned_data)
    return render(request, 'contato/contato.html', contexto)