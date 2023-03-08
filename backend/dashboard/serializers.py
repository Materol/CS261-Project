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

    riskiness = BudgetField()

    class Meta:
        model = Project
        fields = ('id', 'title', 'slug', 'Description', 'Budget', 'riskiness',
                  'StartingDate', 'Deadline', 'Member_size', 'Completed')

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.Description = validated_data.get('Description',
                                                  instance.Description)
        instance.riskiness = validated_data.get('riskiness',
                                                instance.riskiness)
        instance.Budget = validated_data.get('Budget', instance.Budget)
        instance.StartingDate = validated_data.get('StartingDate',
                                                   instance.StartingDate)
        instance.Deadline = validated_data.get('Deadline', instance.Deadline)
        instance.Member_size = validated_data.get('Member_size',
                                                  instance.Member_size)
        instance.Completed = validated_data.get('Completed',
                                                instance.Completed)
        instance.save()
        return instance
