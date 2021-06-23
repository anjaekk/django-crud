import json
from django.http import JsonResponse
from django.views import View
from movies.models import Movie, Actor


class MoviesView(View):
    def get(self, request):
        results = []
        movies = Movie.objects.all()
        for movie in movies:
            actor_arr = []
            actors = movie.actors.all()
            for i in actors:
                actor_arr.append(i.first_name)
            results.append({
                'title' : movie.title,
                'release_date' : movie.release_date,
                'running_time' : movie.running_time,
                'actor' : actor_arr
            })
        return JsonResponse({'results':results}, status=200)
    


class ActorsView(View):
    def get(self, request):
        actors  = Actor.objects.all()
        results = []
        for actor in actors:
            results.append({
                'first_name' : actor.first_name,
                'last_name' : actor.last_name,
                'date_of_birth' : actor.date_of_birth,
                'movies' : list(actor.movies.values('title'))
            })
        return JsonResponse({'results':results}, status=200)
    

