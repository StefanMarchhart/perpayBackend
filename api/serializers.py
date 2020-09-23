from django.contrib.auth.models import User, Group
from api.models import PerpayUser, Payment, Company
from rest_framework import serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerpayUser
        fields = ['url','username', 'email', 'groups']
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']


class TotalSerializer():



    class meta:
        many=True
