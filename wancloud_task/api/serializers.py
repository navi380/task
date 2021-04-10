# Create your views here.
from rest_framework import serializers
from .models import *



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('item_val', 'image')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id','user','item_name', 'location', 'description','status','email', 'phone_number',)
