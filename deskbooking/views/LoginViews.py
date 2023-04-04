from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ..forms import LoginForm
from django.contrib import messages

def user_login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'account.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'You have successfully logged in')
                    return redirect('login')
                else:
                    messages.error(request, 'Your account is disabled')
                    return redirect('login')
            else:
                messages.error(request, 'Invalid login credentials')
                return redirect('login')
        else:
            form = LoginForm()
            return render(request, 'account.html', {'form': form})
