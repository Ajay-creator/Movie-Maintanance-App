from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Movie, Actor
from .serializers import MovieSerializer, ActorSerializer
# Create your views here.


def Home(request):
    context = {}
    return HttpResponse('<h1>Hello</h2>')


class MovieList(APIView):
    """
    List all movies 
    """

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def get_movie(self, pk):
        try:
            return Movie.objects.get(pk=pk)

        except Movie.DoesNotExist:
            raise Http404

    def put(self, request):
        movie = self.get_movie(request.data['id'])
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActorList(APIView):
    """
    List all the actors 
    """

    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)
