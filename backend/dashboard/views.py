from .models import Project
from .serializers import ProjectSerializerDashboard, CreateProjectSerializer
from rest_framework import generics, permissions
from users.models import NewUser

#Training the model

import json
from .predictions.trainer import Trainer
from .predictions.model_knn import ModelKNN
from .predictions.model_naive import ModelNaive
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
     
class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializerDashboard
    queryset = Project.objects.all()


    # def get_queryset(self):
    #     user = self.request.user
    #     return Project.objects.filter(creator=user)
    # def perform_create(self, serializer):
    #     user = self.request.user
    #     serializer.save(creator=user)
 

#Create a project, calculate metrics using KNN model and store in database
class CreateProject(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = CreateProjectSerializer

    def perform_create(self, serializer):

        currentMetric = serializer.validated_data.get('currentMetric') or None
        metricHistory = serializer.validated_data.get('metricHistory') or None
        CSFs = serializer.validated_data.get('CSFs')
        feedback = serializer.validated_data.get('feedback') or None
        if currentMetric is None:
            #csfs = json.loads(CSFs)
            knn_prediction = knn.predict(CSFs)
            json_knn_prediction = to_json_success_metrics(knn_prediction)
            currentMetric = json.loads(json_knn_prediction)
            testFeedback = json.loads(knn.give_feedback(CSFs).get_feedback())
        
        if metricHistory is None:
            metricHistory = currentMetric
        
        if feedback is None:
            feedback = testFeedback
        
        serializer.save(currentMetric=currentMetric, metricHistory=metricHistory, feedback=feedback)


    
class ProjectDetail(generics.RetrieveAPIView):
    serializer_class = ProjectSerializerDashboard
    queryset = Project.objects.all()
    
class DeleteProject(generics.DestroyAPIView):
    serializer_class = ProjectSerializerDashboard
    queryset = Project.objects.all()
