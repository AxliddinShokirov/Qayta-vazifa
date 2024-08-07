from rest_framework.serializers import ModelSerializer
from Front.models import *


class BannerSerializer(ModelSerializer):
    class Meta:

        model=Banner
        fields = '__all__'


class CoachSerializer(ModelSerializer):
    class Meta:
        model=Coach
        fields = '__all__'


class GymSerializer(ModelSerializer):
    class Meta:
        model=Gym
        fields = '__all__'

        

class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields = '__all__'
