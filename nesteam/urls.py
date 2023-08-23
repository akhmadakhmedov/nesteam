from django.contrib import admin
from django.urls import path, include
from games.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'genre', GenreViewSet)
router.register(r'api-studio', StudioViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('games/', games_list, name='games'),
    #path('create-game', CreateGameAPIView.as_view(), name='create-game'),
    path('games/', GameView.as_view(), name='games'),
    path('games-search/', GamesSearchView.as_view(), name='games-search'),
    path('game-create/', GameCreateAPIView.as_view(), name='games'),
    #path('studios/', StudiosListAPIView.as_view()),
    path('users/', include('usersapp.urls')),
    path("collections/", include("collection.urls")),
    path('', include(router.urls)),
]
