from rest_framework import serializers
from quickstart.models import ToDo

from rest_framework import serializers
from quickstart.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ToDo
		fields = ('__all__')