from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from .models import FormDisco


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    
    user = auth.authenticate(request, username=usuario, password=senha)
    
    if not user:
        messages.error(request, 'Usuário ou senha incorreta')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, f'Seja bem vindo(a), {usuario}!')
        return redirect('home')
    

def logout(request):
    auth.logout(request)
    return redirect('index')


def cadastro(request):
    # messages.success(request, 'Requisição feita com sucesso!')
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    # pegar os valores do formulário
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode ficar vazio!')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'A senha deve conter 6 caracteres ou mais')
        return render(request, 'accounts/cadastro.html')

    if len(usuario) < 6:
        messages.error(request, 'O usuário deve conter 6 caracteres ou mais')
        return render(request, 'accounts/cadastro.html')

    if senha != senha2:
        messages.error(request, 'Senhas não conferem. As duas senhas precisam ser iguais')
        return render(request, 'accounts/cadastro.html')

    # para verificar se já existe um usuário com esse mesmo nome:
    if User.objects.filter(username=usuario).exists():
        # username é a chave e usuario é a variável criada ali em cima
        messages.error(request, 'Usuário já existe')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        # email é a chave.
        messages.error(request, 'Email já cadastrado')
        return render(request, 'accounts/cadastro.html')

    # criando o objeto usuário (pegando todos os dados de validação do usuário)
    user = User.objects.create_user(username=usuario, email=email, first_name=nome, password=senha)
    # salvando no sistema
    user.save()

    messages.success(request, 'Cadastro feito com sucesso!')
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormDisco
        return render(request, 'accounts/dashboard.html', {'form': form})
    
    form = FormDisco(request.POST, request.FILES)
    
    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário')
        form = FormDisco(request.POST)
        return render(request, 'accounts/dashboards.html', {'form': form})

    form.save()
    messages.success(request, f'Disco {request.POST.get("album")} salvo com sucesso')
    return redirect('home')
