from django.urls import path 
from . import views
from .views import MyTokenView, MyTokenObtainPairSerializer, LoginAPIView, UserCreateUpdate

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
	# Artists view
	path("", views.ArtistsView.as_view()),
	path("artist/<str:pk>/", views.ArtistsView.as_view()),

	# Albums view
	path("album/", views.AlbumView.as_view()),
	path("album/<str:pk>/", views.AlbumView.as_view()),

	# Musics View
	path("music/", views.MusicView.as_view()),
	path("music/<str:pk>/", views.MusicView.as_view()),


	path("user/", UserCreateUpdate.as_view()),
	path("login/", LoginAPIView.as_view()),

	path('token/', MyTokenView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

