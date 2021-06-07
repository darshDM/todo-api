from rest_framework.views import APIView
from .models import Task
from rest_framework.permissions import AllowAny, IsAdminUser,IsAuthenticated
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import serializers, status


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


# Non generic views for custom operation and response 
# we have to specify custom schema if we use non generic view as swagger will only add request arguments in documentation
class CreateTaskNonGen(APIView):
    serializer_class = TaskSerializer
    def post(self,request,*args,**kwargs):
        if(request.user.is_superuser):
            serializer = TaskSerializer(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class UpdateTaskNonGen(APIView):
    def post(self,request,*args,**kwargs):
        if(request.user.is_superuser):
            task_item = Task.objects.filter(id=request.data['id'])
            task_item.update(request.data)

            serializer = TaskSerializer(data=task_item)
            if(serializer.is_valid()):
                serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)