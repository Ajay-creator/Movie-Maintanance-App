from django.urls import path, include

# views
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('movie_list/', views.MovieList.as_view()),
    path('actor_list/', views.ActorList.as_view()),
]
