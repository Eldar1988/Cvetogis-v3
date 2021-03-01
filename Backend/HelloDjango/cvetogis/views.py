from rest_framework.views import APIView
from rest_framework.response import Response

from shop.serializers import CitySerializer, ReasonsListSerializer, PeopleListSerializer, PresentCategoryListSerializer
from shop.models import City, Reason, People, PresentCategory

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

        return Response(response_data)
