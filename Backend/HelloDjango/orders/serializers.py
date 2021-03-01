from rest_framework import serializers
from .models import CallBack


class CallBackSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallBack
        fields = '__all__'
