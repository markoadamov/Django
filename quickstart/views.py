from django.shortcuts import render
from django.views import View

from rest_framework import mixins, viewsets
from quickstart.models import ToDo
from quickstart.serializers import ToDoSerializer

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class ToDoViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


