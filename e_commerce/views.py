from django.shortcuts import render
from .forms import ContatoForm, LoginForm, RegisterForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model



def index(request):
    context = {
        "titulo": "Index",
        "conteudo": "pagina inicial"
    }
    if request.user.is_authenticated:
        context['logado'] = 'Voce é um usuario premiun'
    else:
        context['logado'] = 'você não está logado'   
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

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
                    "form": form
              }
    print("User logged in")
    if form.is_valid():
        print(f' cleaned data : {form.cleaned_data}')
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password) 
        print(f' está autenticado: {request.user.is_authenticated}')
        print(f'User: {user}')
        #print(request.user.is_authenticated)
        if user is not None:
            #print(request.user.is_authenticated)
            login(request, user)
            print("Login válido")
            print(f' está autenticado: {request.user.is_authenticated}')
            # Redireciona para uma página de sucesso.
            return redirect("/")
        else:
            #Retorna uma mensagem de erro de 'invalid login'.
            print("Login inválido")
    return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        passowrd = form.cleaned_data.get('password')
        #new_user = User.objects.create(username=username, email=email, password=passowrd)
        new_user = User.objects.create_user(username, email, passowrd)
        print(f'novo usuario: {new_user}')

    return render(request, 'auth/register.html', context)