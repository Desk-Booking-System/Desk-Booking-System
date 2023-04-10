<<<<<<< HEAD
from django.shortcuts import render

def errorhandling(request, exception):
    return render(request,'404.html', {})



=======
from django.shortcuts import render

def errorhandling(request, exception):
    return render(request,'404.html', {})



>>>>>>> 8bc4d94d299365771d0309c96207027acaf5437f
# For the custom error 404 page to appear Debug=False in setttings.py