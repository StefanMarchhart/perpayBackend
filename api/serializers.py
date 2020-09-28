from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from api.models import PerpayUser,PerpayUserManager, Payment, Company
from rest_framework import serializers
import re

class PerpayUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = PerpayUser
        fields = ('email', 'username', 'password', 'company')
    
    def validate_email(self, value):
        # Checks to see if the email is in a "Valid" form, and isn't already in use
        regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.search(regex,value):
            raise serializers.ValidationError("Not a valid Email")
        elif PerpayUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already in use!")
        else:
            return value

    def validate_username(self, value):
        # Check to see if the username already exists
        if PerpayUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already in use!")
        else:
            return value

    def validate_password(self, value):
        # Obviously in the real world we'd do a lot more password validation
        if len(value)< 8:
            raise serializers.ValidationError("Password is too short!")
        return value


    def validate_company(self, value):
        # just checking if the company we're claiming to be a part of exists, 
        # regular users wouldn't create new companys anyways

        if not value:
            raise serializers.ValidationError("Company does not exist")
        return value


    def create(self, validated_data):
        print("validated data")
        company = validated_data.pop('company')
        password = validated_data.pop('password')
        username = validated_data.pop('username')
        email = validated_data.pop('email')

        
        print(password)
        print("vaidated")
        user=get_user_model()
        user = PerpayUser.objects.create_user(username=username,email=email,password=password,company=company.id)
        return user
