from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Slider
from .serializers import SliderSerializer

from shop.serializers import CitySerializer, ReasonsListSerializer, PeopleListSerializer, PresentCategoryListSerializer, \
    ProductListSerializer
from shop.models import City, Reason, People, PresentCategory, Product

from shop_settings.models import Course
from shop_settings.serializers import CourseSerializer


class HomePageDataView(APIView):

    def get(self, request):
        response_data = {}
        cities = City.objects.all()
        cities_serializer = CitySerializer(cities, many=True)
        response_data['cities'] = cities_serializer.data

        courses = Course.objects.all()
        courses_serializer = CourseSerializer(courses, many=True)
        response_data['courses'] = courses_serializer.data

        reasons = Reason.objects.all()
        reasons_serializer = ReasonsListSerializer(reasons, many=True)
        response_data['reasons'] = reasons_serializer.data

        peoples = People.objects.all()
        peoples_serializer = PeopleListSerializer(peoples, many=True)
        response_data['peoples'] = peoples_serializer.data

        present_categories = PresentCategory.objects.all()
        present_categories_serializer = PresentCategoryListSerializer(present_categories, many=True)
        response_data['presentCategories'] = present_categories_serializer.data

        slides = Slider.objects.all()
        slides_serializer = SliderSerializer(slides, many=True)
        response_data['slides'] = slides_serializer.data

        return Response(response_data)


class HomeProductsView(APIView):
    """Товары для главной страницы"""

    def get(self, request):
        city = request.GET.get('city')
        response_data = {}
        future_products = Product.objects.filter(future=True, show_on_home_page=True, public=True, set=False,
                                                 in_the_box=False, present=False, cities__slug=city)
        future_products_serializer = ProductListSerializer(future_products, many=True)
        response_data['futureProducts'] = future_products_serializer.data

        return Response(response_data)
