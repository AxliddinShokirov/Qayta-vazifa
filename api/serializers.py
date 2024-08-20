from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
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

class RejaSerializer(ModelSerializer):
    class Meta:
        model=Reja
        fields = '__all__'


class Blog_nameSerializer(ModelSerializer):
    class Meta:
        model=Blog_name
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta:
        model=Contact
        fields = '__all__'


class InfoSerializer(ModelSerializer):
    class Meta:
        model=Info
        fields = '__all__'
    
class CoachSerializer(ModelSerializer):
    class Meta:
        model=Coach
        fields = '__all__'

class GymSerializer(ModelSerializer):
    class Meta:
        model=Gym
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model=Product
        fields = '__all__'
        



