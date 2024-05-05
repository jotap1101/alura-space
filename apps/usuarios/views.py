from apps.usuarios.forms import LoginForm, CadastroForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import redirect, render

# Create your views here.
def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()

        user = auth.authenticate(request=request, username=username, password=password)

        if user is not None:
            auth.login(request, user)

            messages.success(request, 'Login efetuado com sucesso!')

            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos!')

            return redirect('login')

    context = {
        'form': form
    }

    return render(request, 'usuarios/login.html', context)

def logout(request):
    auth.logout(request)

    messages.success(request, 'Logout efetuado com sucesso!')

    return redirect('login')

def cadastro(request):
    form = CadastroForm()

    if request.method == 'POST':
        form = CadastroForm(request.POST)
        
        if form.is_valid():
            username = form['username'].value()
            email = form['email'].value()
            password = form['password1'].value()

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Nome de usuário já cadastrado!')

                return redirect('cadastro')
            
            user = User.objects.create_user(username=username, email=email, password=password)

            user.save()

            messages.success(request, 'Cadastro efetuado com sucesso!')

            return redirect('login')

    context = {
        'form': form
    }

    return render(request, 'usuarios/cadastro.html', context)