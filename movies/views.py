import json
from django.http import JsonResponse
from django.views import View
from movies.models import Movie, Actor


class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results = []
        for movie in movies:
            results.append({
                'title' : movie.title,
                'release_date' : movie.release_date,
                'running_time' : movie.running_time,
                'actor' : list(movie.actors.values('first_name'))
            })
        return JsonResponse({'results':results}, status=200)

class ActorsView(View):
    def get(self, request):
        actors = Actor.objects.all()
        results = []
        for actor in actors:
            results.append({
                'first_name' : actor.first_name,
                'last_name' : actor.last_name,
                'date_of_birth' : actor.date_of_birth,
                'movies' : list(actor.movies.values('title'))
            })
        return JsonResponse({'results':results}, status=200)