from rest_framework import serializers
from .models import ProductOffer,Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name','category', 'price','stock']


class ProductOfferSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = ProductOffer
        fields = ('id','product', 'name', 'price_after_offer', 
                    'discount_percent','updated_at','status')
