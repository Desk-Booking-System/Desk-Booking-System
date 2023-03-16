
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from ..forms import LoginForm
from django.http import HttpResponse
# Create your views here.


def user_login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'account.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            user = authenticate(request,
                                username = cd['username'],
                                password=cd['password'])
           
            if user is not None:
               
                if user.is_active:
                   
                    login(request, user)
                   
                    return HttpResponse("Authentication Successful")
                else:
                   
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
        else:
            form = LoginForm()
            return render(request, 'account.html', {'form': form})
      

# def view_page(request):
#     if request.method == "GET":
#         form = LoginForm()
#         return render(request, 'account.html', {'form': form})