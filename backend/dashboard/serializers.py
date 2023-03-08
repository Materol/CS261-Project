from rest_framework import serializers
from .models import Project
from django.conf import settings
from users.models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = NewUser
        fields = ('id', 'user_name', 'projects', 'owner')



class BudgetField(serializers.Field):

    def to_representation(self, value):
        # You can decide here how you want to return your data back
        return value

    def to_internal_value(self, data):
        # this will be passed to validated_data, so will be used to create/update instances
        # you could do some validation here to make sure it is a float
        # https://www.django-rest-framework.org/api-guide/fields/#raising-validation-errors
        return int(int(data) / 100)


#This is where the attirbutes from the Database schema should be placed
class ProjectSerializerDashboard(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ('id', 'name', 'Description', 'currentMetric', 'metricHistory', 'members')
          
              
    def create(self, validated_data):
        return Project.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.Description = validated_data.get('Description', instance.Description)
        instance.currentMetric = validated_data.get('currentMetric', instance.currentMetric)
        instance.metricHistory = validated_data.get('metricHistory', instance.metricHistory)
        instance.members = validated_data.get('members', instance.members)
        instance.save()
        return instance
    
    
class CreateProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ('id', 'name', 'Description', 'currentMetric','metricHistory', 'members')
          
              
    def create(self, validated_data):
        return Project.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.Description = validated_data.get('Description', instance.Description)
        instance.currentMetric = validated_data.get('currentMetric', instance.currentMetric)
        instance.metricHistory = validated_data.get('metricHistory', instance.metricHistory)
        instance.members = validated_data.get('members', instance.members)
        instance.save()
        return instance