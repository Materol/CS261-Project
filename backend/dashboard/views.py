import json
import time

from .models import Project
from .serializers import ProjectSerializerDashboard, CreateProjectSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response



from .predictions.trainer import Trainer
from .predictions.model_knn import ModelKNN
from .predictions.utils import to_json_success_metrics

# Trainer class is used to train only the KNN model right now. Run this upon
# initialising the server as this loads the dataset and is slow.
trainer = Trainer(seed=415324)

# K-Nearest Neighbours model needs to be trained. The simplest way to do this is
# to use the Trainer class. Run these lines of code in the initialisation of the
# server as training takes a long time.
knn = ModelKNN()
trainer.train_model(knn)

# Create your views here.


#View for the dashboard - viewing multiple projects
class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializerDashboard

    def get_queryset(self):
        email = self.kwargs.get('user_email')

        # Filter by owner email column `owner`
        queryset = Project.objects.filter(owner=email)
        return queryset


#Create a project, calculate metrics using KNN model and store in database
class CreateProject(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = CreateProjectSerializer

    #Override create from generics, add KNN metric calculation
    def perform_create(self, serializer):

        # Get inputted data
        currentMetric = serializer.validated_data.get('currentMetric') or None
        metricHistory = serializer.validated_data.get('metricHistory') or None
        CSFs = serializer.validated_data.get('CSFs')
        feedback = serializer.validated_data.get('feedback') or None
        feedbackHistory = serializer.validated_data.get('feedbackHistory') or None
        owner = serializer.validated_data.get('owner')

        # Current Metric should be empty by default as there is no entry on
        # frontend form, must be calculated
        if currentMetric is None:
            knn_prediction = knn.predict(CSFs)
            json_knn_prediction = to_json_success_metrics(knn_prediction)
            currentMetric = json.loads(json_knn_prediction)
            feedback = json.loads(knn.give_feedback(CSFs).get_feedback())

        # Get the unix timestamp
        timestamp = int(time.time())

        # Create a json mapping timestamp to the metrics for history
        if metricHistory is None:
            metricHistory = {timestamp: currentMetric}
        else:
            metricHistory = json.loads(metricHistory)
            metricHistory[timestamp] = currentMetric

        # Create a json mapping timestamp to the feedback for history
        if feedbackHistory is None:
            feedbackHistory = {timestamp: feedback}
        else:
            feedbackHistory = json.loads(feedbackHistory)
            feedbackHistory[timestamp] = feedback

        serializer.save(owner=owner,
                        currentMetric=currentMetric,
                        metricHistory=metricHistory,
                        feedback=feedback,
                        feedbackHistory=feedbackHistory)


#View for a single project in detail
class ProjectDetail(generics.RetrieveAPIView):
    serializer_class = ProjectSerializerDashboard
    queryset = Project.objects.all()


#View for deleteing a project
class DeleteProject(generics.DestroyAPIView):
    serializer_class = ProjectSerializerDashboard
    queryset = Project.objects.all()

# Update a project
class UpdateProject(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProjectSerializerDashboard
    queryset = Project.objects.all()
    allowed_methods = ['PUT', 'POST']
    lookup_field = 'pk'

    def post(self, request, pk, format=None):
        # Add your implementation for POST requests here
        print("were in the post")
        print(pk)
        print(request.data)
        instance = Project.objects.get(pk=pk)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.update_fields(serializer)
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update_fields(self, serializer):
        # Get inputted data
        metricHistory = serializer.validated_data.get('metricHistory') or None
        CSFs = serializer.validated_data.get('CSFs')
        feedbackHistory = serializer.validated_data.get('feedbackHistory') or None
        description = serializer.validated_data.get('description')
        name = serializer.validated_data.get('name')
        members = serializer.validated_data.get('members')

        # Update prediction and feedback
        knn_prediction = knn.predict(CSFs)
        json_knn_prediction = to_json_success_metrics(knn_prediction)
        currentMetric = json.loads(json_knn_prediction)
        feedback = json.loads(knn.give_feedback(CSFs).get_feedback())

        # Get the unix timestamp
        timestamp = int(time.time())

        # Create a json mapping timestamp to the metrics for history
        if metricHistory is None:
            metricHistory = {timestamp: currentMetric}
        else:
            metricHistory = json.loads(metricHistory)
            metricHistory[timestamp] = currentMetric

        # Create a json mapping timestamp to the feedback for history
        if feedbackHistory is None:
            feedbackHistory = {timestamp: feedback}
        else:
            feedbackHistory = json.loads(feedbackHistory)
            feedbackHistory[timestamp] = feedback

        serializer.save(name=name,
                        description=description,
                        CSFs=CSFs,
                        currentMetric=currentMetric,
                        metricHistory=metricHistory,
                        feedback=feedback,
                        feedbackHistory=feedbackHistory,
                        members=members)
