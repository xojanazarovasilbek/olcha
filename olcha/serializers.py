from rest_framework import serializers
from olcha.models import Category, Product, Image


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ()

class ProductSerializers(serializers.ModelSerializer):
    image_count = serializers.SerializerMethodField()
    primary_image = serializers.SerializerMethodField()
    
    def get_primary_image(self, product):
        if product.images:
            image = product.images.filter(is_primary = True)
            return image.image.url
        return None
    
    def get_image_count(self, obj):
        return obj.images.count()
    class Meta:
        model = Product
        fields = ('id','name','desc','price','stock','discount','category','image_count')




