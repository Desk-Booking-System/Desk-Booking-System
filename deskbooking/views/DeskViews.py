from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from requests import post
from deskbooking.MODELS.models import Desk
from ..serializer import DeskSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
from ..forms import DeskForm


@api_view(['GET', 'POST'])

@csrf_exempt
def add_desk(request):
    
        
    if request.method == "POST":
        serializer = DeskSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=status.HTTP_200_OK)
        else:
            return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse(request)
    


def Desks(request):
    desks = Desk.objects.all()
    form = DeskForm()
    # desk_id = Desk.objects.get(desk_id=request.POST['desk_id'])
    if request.method == "GET":
        return render(request , "deskbook.html", {"desks":desks, "deskform":form} )
   

    elif request.method == "POST":
        print(request.POST.get['hidden_id'])
        # context = {}
        # obj = get_object_or_404(Desk, desk_id=desk_id)
        # form = form(request.POST or None, instance = obj)
        # if form.is_valid():
        #     form.save()
        #     return HttpResponseRedirect("deskbook.html")
        # context["form"] = form
        # return render(request,"deskbook.html" ,{"desks":desks, "deskform":form})
        return HttpResponse(request, status=status.HTTP_200_OK)

    else:
        return HttpResponse("bad request", status=status.HTTP_400_BAD_REQUEST)
        
   



