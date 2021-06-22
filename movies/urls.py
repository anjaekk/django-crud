from django.urls import path
from movies.views import MoviesView, ActorsView

urlpatterns = [
    path('/movies', MoviesView.as_view()),
    path('/actors', ActorsView.as_view()),
]
