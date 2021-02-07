from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password

class CustomerSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        return make_password(value)
    class Meta:
        model=models.User
        fields = ["email","username","password",]
        extra_kwargs = {
            'password': {'style': {'input_type': 'password'}}
        }
        def create(self,validated_data):
            user=models.User.objects.create_user(
                email=validated_data['email'],
                username=validated_data['username'],
                password=validated_data['password']
            )
            return user;


class RentACarSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.RentCar
        fields='__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Vehicles
        fields='__all__'
