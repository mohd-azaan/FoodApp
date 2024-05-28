from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth import logout 
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def custom_logout(request):
    logout(request)
    return render(request, 'users/logout.html')
    
@login_required
def profilePage(request):
    return render(request, 'users/profile.html')

