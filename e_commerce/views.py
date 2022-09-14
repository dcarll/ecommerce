from django.shortcuts import render

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
    return render(request, 'about.html', contexto)

def contato(request):
    contexto = {
        "titulo": "contato",
        "conteudo": "pagina de contato"
    }
    return render(request, 'contato.html', contexto)