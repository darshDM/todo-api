from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Task

#using model serializer to validate data according to model.
class TaskSerializer(serializers.ModelSerializer):
    class Meta():
        model = Task
        fields = '__all__'

    