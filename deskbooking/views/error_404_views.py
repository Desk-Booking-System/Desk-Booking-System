from django.shortcuts import render

def errorhandling(request, exception):
    return render(request,'404.html', {})

# For the custom error 404 page to appear Debug=False in setttings.py