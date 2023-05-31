from django.shortcuts import render
from django.views import View

from rest_framework import mixins, viewsets
from quickstart.models import ToDo
from quickstart.serializers import ToDoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

from django.contrib.auth.models import User

from rest_framework.permissions import IsAdminUser

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class ToDoViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class UserViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserFilterView(APIView):
    def get(self, request):
        name = request.GET.get('name', '')
        filtered_users = User.objects.filter(first_name__icontains=name) | User.objects.filter(last_name__icontains=name)
        serializer = UserSerializer(filtered_users, many=True)
        return Response(serializer.data)

