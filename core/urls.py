from django.urls import path
from .views import CreateTask, getTaskList,getSingleItem,UpdateTaskView,DeleteTaskView

urlpatterns = [
    path('get/<int:pk>',getSingleItem.as_view()),
    path('getall',getTaskList.as_view()),
    path('put/<int:pk>',UpdateTaskView.as_view()),
    path('create',CreateTask.as_view()),
    path('delete/<int:pk>',DeleteTaskView.as_view())
]
