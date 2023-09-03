from rest_framework import serializers
from blog.models import SightseeingPlaces,Category
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class SightseeingPlacesSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    author = UserSerializer(many=False)
    class Meta:
        model = SightseeingPlaces
        fields = '__all__'

