from rest_framework import serializers
from .models import Actor, Movie, MovieActorRelation


class MovieSerializer(serializers.ModelSerializer):

    no_of_actors = serializers.SerializerMethodField('get_no_of_actors')

    class Meta:
        model = Movie
        fields = '__all__'

    def get_no_of_actors(self, movie):
        actors = MovieActorRelation.objects.filter(movie=movie)
        return len(actors)


class ActorSerializer(serializers.ModelSerializer):

    no_of_movies = serializers.SerializerMethodField('get_no_of_movies')

    class Meta:
        model = Actor
        fields = '__all__'

    def get_no_of_movies(self, actor):
        movies = MovieActorRelation.objects.filter(actor=actor)
        return len(movies)
