from django.urls import path

from . import views

urlpatterns = [
	path('predictTweet/', views.predictTweet, name='predictTweet'),
	path('predict/', views.predict, name='predict'),


]
