from django.urls import path, include
from rest_framework import routers
from .views import *


collection_router = routers.DefaultRouter()
collection_router.register(r'', CollectionViewSet)


urlpatterns = [
    path('',include(collection_router.urls)),
    ]