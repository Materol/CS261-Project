
#Serializers will return data in the right format from the database to REACT

from rest_framework import serializers
from dashboard.models import Project
from django.conf import settings



#This is where the attirbutes from the Database schema should be placed
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'slug', 'creator','Description')


#Simple user model, can be replaced by schema if necessary
class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}
