from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api-users', UserViewSet)


urlpatterns = [
    path('list/', users_list, name='users-list'),
    path('detail/<int:pk>/', user_detail, name='user-detail'),
    path('user-router/', include(router.urls)),
    path('players/', PlayerListAPIView.as_view(), name='players'),
]