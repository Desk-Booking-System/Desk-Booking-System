from django.shortcuts import render
from ..MODELS.models import Desk

def desk_booking(request):
    desks = Desk.objects.filter(is_available=True)
    return render(request, 'deskbook.html', {'desks': desks})
