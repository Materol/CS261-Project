#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


#from rest_framework import serializers
#from .models import CustomUser




#class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

#    @classmethod
#    def get_token(cls, user):
#        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
#        token['fav_color'] = user.fav_color
#        return token



#class CustomUserSerializer(serializers.ModelSerializer):
#    """
#    Currently unused in preference of the below.
#    """
#    email = serializers.EmailField(
#        required=True
#    )
#    username = serializers.CharField()
#    password = serializers.CharField(min_length=8, write_only=True)

#    class Meta:
#        model = CustomUser
#        fields = ('email', 'username', 'password')
#        extra_kwargs = {'password': {'write_only': True}}

#    def create(self, validated_data):
#        password = validated_data.pop('password', None)
#        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
#        if password is not None:
#            instance.set_password(password)
#        instance.save()
#        return instance

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