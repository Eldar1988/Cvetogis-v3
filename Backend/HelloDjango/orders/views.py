from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CallBack
from .serializers import CallBackSerializer


class CreateCallBackView(APIView):

    def post(self, request):
        print(request.data)
        serializer = CallBackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        print(serializer.errors)

        return Response(status=400)
