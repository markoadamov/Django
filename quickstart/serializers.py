from rest_framework import serializers
from quickstart.models import ToDo
from django.contrib.auth import get_user_model

class ToDoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ToDo
		fields = ('__all__')

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
