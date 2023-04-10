from urllib import request
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from deskbooking.MODELS.models import Desk

from ..views import LoginViews

@csrf_exempt
# def rend_desk(request):
    # if request.method == "GET":
        # desk=Desk.objects.all()
        # is_desk = request.GET.get('desk_name')
        # return HttpResponse(is_desk)
    # elif request.method == "PUT":
        # desk=Desk()
        # desk.is_available = False
        # desk.date = request.POST.get('date')
        # desk.employee_reserved_name = request.POST.get('employee_reserve_name')
        # desk.save()
        # return HttpResponse("ok")

@csrf_exempt
def add_desk(request):
    if request.method == "POST":
        desk=Desk()
        desk.desk_name= request.POST.get('desk_name')
        desk.is_available= request.POST.get('is_available')
        desk.save()
    return HttpResponse(request)
