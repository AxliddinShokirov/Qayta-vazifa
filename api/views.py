from Front.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView

class BannerView(APIView):
    serializer=BannerSerializer
    queryset=Banner

    def get(self, request, *args, **kwargs):
      banners=self.queryset.all()
      serializer=self.serializer(banners, many=True)
      return Response(serializer.data)
    

    def post(self, request, *args, **kwargs):
        serializers=self.serializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
        return Response(serializers.data)

    def put(self, request,id, *args, **kwargs):
       queryset=Banner.objects.get(id=id)
       serializr_data=BannerSerializer(
           queryset,
           data=request.data
       )
       if serializr_data.is_valid():
          serializr_data.save()
       return Response(serializr_data.data)

    def delete(self, request, id, *args, **kwargs):
        queryset=Banner.objects.get(id=id)
        queryset.delete()
        return Response({'status':200})
    

class CategoryView(APIView):
    serializer=CategorySerializer
    queryset=Category
    
    def get(self, request, *args, **kwargs):
        categories=Category.objects.all()
        serializer=self.serializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializers=self.serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)
    
    def put(self, request, id, *args, **kwargs):
        queryset=Category.objects.get(id=id)
        serializer_data=CategorySerializer(
            queryset,
            data=request.data
        )
        if serializer_data.is_valid():
            serializer_data.save()
        return Response(serializer_data.data)
    
    def delete(self, request, id, *args, **kwargs):
        queryset=Category.objects.get(id=id)
        queryset.delete()
        return Response({'status':200})

class GymView(APIView):
    serializer=GymSerializer
    queryset=Gym
    
    def get(self, request, *args, **kwargs):
        gyms=Gym.objects.all()
        serializer=self.serializer(gyms, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializers=self.serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)
    
    def put(self, request, id, *args, **kwargs):
        queryset=Gym.objects.get(id=id)
        serializer_data=GymSerializer(
            queryset,
            data=request.data
        )
        if serializer_data.is_valid():
            serializer_data.save()
        return Response(serializer_data.data)
    
    def delete(self, request, id, *args, **kwargs):
        queryset=Gym.objects.get(id=id)
        queryset.delete()
        return Response({'status':200})

class CoachView(APIView):
    serializer=CoachSerializer
    queryset=Coach
    
    def get(self, request, *args, **kwargs):
        coaches=Coach.objects.all() 
        serializer=self.serializer(coaches, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializers=self.serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)
    
    def put(self, request, id, *args, **kwargs):
        queryset=Coach.objects.get(id=id)
        serializer_data=CoachSerializer(
            queryset,
            data=request.data
        )
        if serializer_data.is_valid():
            serializer_data.save()
        return Response(serializer_data.data)
    
    def delete(self, request, id, *args, **kwargs):
        queryset=Coach.objects.get(id=id)
        queryset.delete()
        return Response({'status':200})
    
class ProductView(APIView):
    serializer=ProductSerializer
    queryset=Product
    
    def get(self, request, *args, **kwargs):
        products=Product.objects.all()
        serializer=self.serializer(products, many=True)
        return Response(serializer.data)    
    

    def post(self, request, *args, **kwargs):
        serializers=self.serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)
    
    def put(self, request, id, *args, **kwargs):

        queryset=Product.objects.get(id=id)
        serializer_data=ProductSerializer(
            queryset,
            data=request.data
        )
        if serializer_data.is_valid():
            serializer_data.save()
        return Response(serializer_data.data)
    
    def delete(self, request, id, *args, **kwargs):
        queryset=Product.objects.get(id=id)
        queryset.delete()
        return Response({'status':200})

class InfoView(APIView):
        serializer=InfoSerializer
        queryset=Info
        
        def get(self, request, *args, **kwargs):
            infos=Info.objects.all()
            serializer=self.serializer(infos, many=True)
            return Response(serializer.data)
        
        def post(self, request, *args, **kwargs):
            serializers=self.serializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
            return Response(serializers.data)
        
        def put(self, request, id, *args, **kwargs):
            queryset=Info.objects.get(id=id)
            serializer_data=InfoSerializer(
                queryset,
                data=request.data
            )
            if serializer_data.is_valid():
                serializer_data.save()
            return Response(serializer_data.data)
        
        def delete(self, request, id, *args, **kwargs):
            queryset=Info.objects.get(id=id)
            queryset.delete()
            return Response({'status':200})

class RejaView(APIView):
    serializer=RejaSerializer
    queryset=Reja
    
    def get(self, request, *args, **kwargs):
        rejas=Reja.objects.all()
        serializer=self.serializer(rejas, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializers=self.serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)
    
    def put(self, request, id, *args, **kwargs):
        queryset=Reja.objects.get(id=id)
        serializer_data=RejaSerializer(
            queryset,
            data=request.data
        )
        if serializer_data.is_valid():
            serializer_data.save()
        return Response(serializer_data.data)
    
    def delete(self, request, id, *args, **kwargs):
        queryset=Reja.objects.get(id=id)
        queryset.delete()
        return Response({'status':200}) 

       
       
