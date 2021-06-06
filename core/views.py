from typing import List
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Task
from rest_framework.permissions import AllowAny, IsAdminUser,IsAuthenticated
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status


#provides list of all task using generic listView
class getTaskList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

#provides single item 
class getSingleItem(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        item = Task.objects.get(id=pk)

        #serializing task for transmission
        item = TaskSerializer(item).data
        return Response(data=item,status=status.HTTP_200_OK)


# using generic view for all create, update and delete operations
class CreateTask(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TaskSerializer


class UpdateTaskView(UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class DeleteTaskView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()