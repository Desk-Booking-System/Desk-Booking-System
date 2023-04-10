<<<<<<< HEAD
from django.shortcuts import render
from ..MODELS.models import Desk

def desk_booking(request):
    desks = Desk.objects.filter(is_available=True)
    return render(request, 'deskbook.html', {'desks': desks})
=======
from django.shortcuts import render
from ..MODELS.models import Desk

def desk_booking(request):
    desks = Desk.objects.filter(is_available=True)
    return render(request, 'deskbook.html', {'desks': desks})
>>>>>>> 8bc4d94d299365771d0309c96207027acaf5437f
