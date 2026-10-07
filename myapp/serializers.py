from rest_framework import serializers
from .models import *


class Studentserializers(serializers.ModelSerializer):
    age_afterten=serializers.IntegerField(read_only=True)
    class Meta:
        model = Student
        fields = '__all__'

    def validate_age(self,value):
            if value < 5 or value >100:
                raise serializers.ValidationError(
                    "age must be between 5 and 100"
                )
            return value

    def validate(self, data):
        if data ["course"]=="data science" and data["age"]<18:
            raise serializers.ValidationError(
                "Student must be at least 18 for Data Science"
            )
        return data

    

    

class Employeeserializers(serializers.ModelSerializer):
    age_ofteen = serializers.IntegerField(read_only=True)   
    class Meta:
        model = Employee
        fields = "__all__"
class Movieserializers(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields="__all__"
class Productserializers(serializers.ModelSerializer):
    price_afterten=serializers.IntegerField(read_only=True)
    class Meta:
        model=Product
        fields="__all__"



class Bookserializers(serializers.ModelSerializer):
    published_year_afterten=serializers.IntegerField(read_only=True)
    class Meta:
        model=Book
        fields="__all__"


class staffserialzer(serializers.ModelSerializer):
    class Mata:
        model:Staffs
        fileds="__all__"

class Staffpostserilazer(serializers.ModelSerializer):
    class Meta:
        model:Staffs
        fields="__all__"

class imageseralizer(serializers.ModelSerializer):
    class Meta:
        model=Images
        fields="__all__"

from django.contrib.auth.models import User
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user= User.objects.create_user(**validated_data)
        return user
        