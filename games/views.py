from rest_framework.generics import ListCreateAPIView
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


#def games_list(request):
#    game_lst = Game.objects.all()
#    serializer = GameSerializer(game_lst, many=True)
#    data = serializer.data
#    return JsonResponse(data, safe=False)

#class StudiosListAPIView(ListAPIView):
#    queryset = Studio.objects.all()
#    serializer_class = StudioSerializer


#class CreateGameAPIView(CreateAPIView):
#    queryset = Game.objects.all()
#    serializer_class = GameSerializer

class GameView(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class StudioViewSet(ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

class GameCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = GameSerializer(data=data)
        if serializer.is_valid():
            game = Game()
            game.name = serializer.validated_data['name']
            game.year = serializer.validated_data['year']
            game.genre = serializer.validated_data['genre']
            game.studio= serializer.validated_data['studio']
            game.save()
            serializer = GameSerializer(instance=game)
            return Response(serializer.data,
                            status=201
                            )
        else:
            errors = serializer.error_messages
            response_data={
                "message": "Not valid data",
                'errors': errors
            }
            return Response(
                data=response_data,
                status=400
            )

class GamesSearchView(APIView):
    def get(self, request):
        if 'key_word' in request.GET:
            key_word = request.GET['key_word']
        elif 'key_word' in request.data:
            key_word = request.data['key_word']
        else:
            return Response('no data', status = 400)

        games = Game.objects.filter(
            Q(name__icontains=key_word) |
            Q(genre__name__icontains=key_word) |
            Q(studio__name__icontains=key_word)
        )

        serializer = GameSerializer(instance=games, many=True)
        json_data = serializer.data
        return Response(data=json_data)