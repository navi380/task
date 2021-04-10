from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def found_items(request):
    found_items_list = Item.objects.filter(status='found')
    serializer = ItemSerializer(found_items_list, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def lost_items(request):
    lost_items_list = Item.objects.filter(status='lost')
    serializer = ItemSerializer(lost_items_list, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def add_item(request):
    if request.method == 'POST':
        files = request.FILES.getlist('image')
        data = request.data
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            current_item = Item.objects.get(id=serializer.data['id'])
            for f in files:
                Images.objects.create(item_val=current_item, image=f)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@permission_classes((IsAuthenticated, ))
def detail_update_or_delete(request, id):
    try:
        item_instance = Item.objects.get(pk=id)
    except ObjectDoesNotExist:
        item_instance = None

    if request.method == 'GET':
        serializer = ItemSerializer(item_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        files = request.FILES.getlist('image')
        data = request.data
        serializer = ItemSerializer(item_instance, data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            current_item = Item.objects.get(id=serializer.data['id'])
            for f in files:
                Images.objects.create(item_val=current_item, image=f)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        item_instance.delete()
        return Response(status=204)