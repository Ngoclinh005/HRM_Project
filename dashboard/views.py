from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard_home')

    error = ''

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard_home')
        else:
            error = 'Tên đăng nhập hoặc mật khẩu không đúng!'

    return render(request, 'dashboard/login.html', {'error': error})


@login_required(login_url='login')
def dashboard_home(request):
    display_name = request.user.get_full_name() or request.user.username

    return render(request, 'dashboard/index.html', {
        'display_name': display_name
    })


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def employees_view(request):
    display_name = request.user.get_full_name() or request.user.username

    return render(request, 'dashboard/employees.html', {
        'display_name': display_name
    })