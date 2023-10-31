from django.http import JsonResponse, HttpResponse
from django.contrib.auth import login, logout, authenticate
from rest_framework import generics, mixins

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import Artist, Album, Music, User
from .serializers import ArtistSerializer, AlbumSerializer, MusicSerializer, UserSerializer, LoginSerializer
# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff
        token['token'] = user.token
        
        # ...
        return token
class MyTokenView(TokenObtainPairView):
	serializer_class  = MyTokenObtainPairSerializer

	

class ArtistsView(
	mixins.ListModelMixin, 
	mixins.RetrieveModelMixin, 
	mixins.CreateModelMixin, 
	mixins.UpdateModelMixin,
	mixins.DestroyModelMixin, 
	generics.GenericAPIView):

	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer
	# lookup_field = "pk"

	def get(self, request, *args, **kwargs):
		pk = kwargs.get("pk")
		if pk is not None:
			return self.retrieve(request, *args, **kwargs)
		return self.list(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

# artists_view = ArtistsView.as_view()

class MusicView(
	mixins.ListModelMixin,
	mixins.CreateModelMixin,
	mixins.RetrieveModelMixin, 
	mixins.UpdateModelMixin,
	mixins.DestroyModelMixin, 
	generics.GenericAPIView):

	queryset = Music.objects.all()
	serializer_class = MusicSerializer
	lookup_field = "pk"
	def get(self, request, *args, **kwargs):
		pk = kwargs.get("pk")
		if pk is not None:
			return self.retrieve(request, *args, **kwargs)
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

# music_view = MusicView.as_view()

class AlbumView(
	mixins.ListModelMixin, 
	mixins.RetrieveModelMixin, 
	mixins.CreateModelMixin, 
	mixins.UpdateModelMixin,
	mixins.DestroyModelMixin, 
	generics.GenericAPIView):

	queryset = Album.objects.all()
	serializer_class = AlbumSerializer
	# lookup_field = "pk"

	def get(self, request, *args, **kwargs):
		pk = kwargs.get("pk")
		if pk is not None:
			return self.retrieve(request, *args, **kwargs)
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


class UserCreateUpdate(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
	mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

	queryset = User.objects.all()
	serializer_class = UserSerializer

	lookup_field = "pk"

	def get(self, request, *args, **kwargs):
		if kwargs.get("pk") is not None:
			return self.retrieve(request, *args, **kwargs)
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class LoginAPIView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
	queryset = User.objects.all()
	serializer_class = LoginSerializer
	authentication_classes = [TokenAuthentication]

	def post(self, request, *args, **kwargs):
		email = request.data.get('email')
		password = request.data.get('password')
		user = authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			refresh = RefreshToken.for_user(user)
			request.user.token = str(refresh.access_token)
			request.user.save()
			return Response({'id':user.id, 'token':user.token, 'first_name':user.first_name,'last_name':user.last_name, 'phone_number': user.phone_number, 'email':user.email, 'password':user.password, 'username':user.username})
			# return HttpResponse("Logged in successfully")
		return HttpResponse("Password or email is not correct")


# album_view = AlbumView.as_view()
