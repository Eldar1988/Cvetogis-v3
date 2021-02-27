from rest_framework import serializers

from .models import City, Reason, Sort, Product, DeliveryBranch, Image, PresentCategory


class DeliveryBranchSerializer(serializers.ModelSerializer):
    """Районы доставки"""

    class Meta:
        model = DeliveryBranch
        exclude = ('order',)


class CitySerializer(serializers.ModelSerializer):
    """Города"""
    deliveries = DeliveryBranchSerializer(many=True)

    class Meta:
        model = City
        fields = '__all__'


class ReasonsListSerializer(serializers.ModelSerializer):
    """Поводы список"""

    class Meta:
        model = Reason
        exclude = ('description', 'order')


class PresentCategoryListSerializer(serializers.ModelSerializer):
    """Категории подарков список"""

    class Meta:
        model = PresentCategory
        exclude = ('order',)


class SortListSerializer(serializers.ModelSerializer):
    """Сорта список"""

    class Meta:
        model = Sort
        exclude = ('order',)


class ProductListSerializer(serializers.ModelSerializer):
    """Список товаров"""
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = Product
        exclude = ('description', 'future', 'show_on_home_page', 'order',
                   'seller', 'public', 'views', 'pub_date', 'update')


class ProductImagesSerializer(serializers.ModelSerializer):
    """Дополнительные изображения товара"""
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = Image
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    """Детали товара"""
    sort = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)
    images = ProductImagesSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = Product
        exclude = ('pub_date', 'update', 'views', 'public', 'order', 'show_on_home_page', 'future')