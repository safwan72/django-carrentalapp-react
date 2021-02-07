from django.shortcuts import render
from . import models, serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# Create your views here.
class RentACarViewSerializer(ModelViewSet):
    serializer_class = serializers.RentACarSerializer
    queryset = models.RentCar.objects.all()


class ViewCarSerializer(ModelViewSet):
    serializer_class = serializers.VehicleSerializer
    queryset = models.Vehicles.objects.all()
    
    
class NewUserSerializer(ModelViewSet):
    serializer_class = serializers.CustomerSerializer
    queryset = models.User.objects.all()
