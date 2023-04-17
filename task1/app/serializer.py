from rest_framework import serializers
from .models import Buyer,Seller,Items

class Buyerseri(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['name','phone','address']

class Sellerseri(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['name','phone','address']
        
        
class Itemseri(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['name','quantity','price']
    
    
        

