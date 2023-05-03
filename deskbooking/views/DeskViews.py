from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from deskbooking.MODELS.models import Desk
from ..serializer import DeskSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
import json


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
    return render(request , "deskbook.html", {"desks":desks} )