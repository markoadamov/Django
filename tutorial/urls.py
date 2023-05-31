"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from quickstart.views import HomeView
from quickstart.views import ToDoViewSet

from rest_framework_simplejwt.views import TokenObtainPairView

from quickstart.views import UserProfileView
from quickstart.views import UserViewSet
from quickstart.views import UserTemplateView

from quickstart.views import UserFilterView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),
    path('todo/<int:pk>/', ToDoViewSet.as_view({'get': 'retrieve'}), name='todo-detail'),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/me/', UserProfileView.as_view(), name='user_profile'),

    # path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve'}), name='user_details'),
    path('users/<int:pk>/', UserTemplateView.as_view(), name='user-template'),

    path('users/filter/', UserFilterView.as_view(), name='user-filter'),
]
