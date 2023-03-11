from rest_framework import serializers
from .models import Project
from django.conf import settings
from users.models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Project.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = NewUser
        fields = ('id', 'user_name', 'projects', 'owner')


#Serializer for project reading
class ProjectSerializerDashboard(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'description',
            'CSFs',
            'currentMetric',
            'metricHistory',
            'feedback',
            'members',
            'feedbackHistory',
        )

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.CSFs = validated_data.get('CSFs', instance.CSFs)
        instance.currentMetric = validated_data.get('currentMetric',
                                                    instance.currentMetric)
        instance.metricHistory = validated_data.get('metricHistory',
                                                    instance.metricHistory)
        instance.feedback = validated_data.get('feedback', instance.feedback)
        instance.feedbackHistory = validated_data.get('feedbackHistory',
                                                      instance.feedbackHistory)
        instance.members = validated_data.get('members', instance.members)
        instance.save()
        return instance


#Serializer for project creation
class CreateProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'description',
            'CSFs',
            'currentMetric',
            'metricHistory',
            'feedback',
            'members',
            'owner',
            'feedbackHistory',
        )

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.CSFs = validated_data.get('CSFs', instance.CSFs)
        instance.currentMetric = validated_data.get('currentMetric',
                                                    instance.currentMetric)
        instance.metricHistory = validated_data.get('metricHistory',
                                                    instance.metricHistory)
        instance.feedback = validated_data.get('feedback', instance.feedback)
        instance.feedbackHistory = validated_data.get('feedbackHistory',
                                                      instance.feedbackHistory)
        instance.members = validated_data.get('members', instance.members)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
