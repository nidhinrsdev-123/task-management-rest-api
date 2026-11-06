from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Task
class RegisterSerializer(serializers.ModelSerializer):
 password=serializers.CharField(write_only=True,min_length=8)
 class Meta:
  model=get_user_model(); fields=("id","username","email","password")
 def create(self,validated_data): return get_user_model().objects.create_user(**validated_data)
class TaskSerializer(serializers.ModelSerializer):
 owner=serializers.ReadOnlyField(source="owner.username")
 class Meta:
  model=Task; fields=("id","owner","title","description","status","priority","due_date","created_at","updated_at")
  read_only_fields=("id","owner","created_at","updated_at")
 def validate_title(self,value):
  value=value.strip()
  if not value: raise serializers.ValidationError("Title cannot be blank.")
  return value
