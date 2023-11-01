from rest_framework import serializers
from .models import *


class MusicSerializer(serializers.ModelSerializer):
	class Meta:
		model = Music  
		fields = ["id", "music_name", "artist_name", "album_name", "genre_type", "musics_type", "edited_by"]


class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre 
		fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
	musics_list = MusicSerializer(many=True, read_only=True)
	total_music = serializers.SerializerMethodField()
	class Meta:
		model = Album 
		fields = ["id", "album_name", "artist_name", "avatar", "total_music", "musics_list"]

	def get_total_music(self, obj):
		return obj.music_set.count()

class ArtistSerializer(serializers.ModelSerializer):
	album_lists = AlbumSerializer(many=True, read_only=True)
	total_album = serializers.SerializerMethodField()
	class Meta:
		model = Artist  
		fields = ["id", "artist_name", "artist_phone", "address", "total_album", "album_lists"]

	def get_total_album(self, obj):
		return obj.album_set.count()




class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=100, write_only=True, required=True, style={'input_type': 'password'})
	token = serializers.CharField(max_length=500, read_only=True)

	class Meta:
		model = User
		fields = ['id' ,'first_name', 'last_name', 'username', 'email', 'phone_number', 'password', 'token', 'is_staff', 'is_superuser', 'groups', 'user_permissions']

	def create(self, validated_data):
		user = super().create(validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user


	def update(self, instance, validated_data):
		user = super().update(instance, validated_data)
		try:
			user.set_password(validated_data['password'])
			user.save()
		except KeyError:
			pass
		return user

	


class LoginSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=100, write_only=True, required=True, style={'input_type': 'password'})
	tokens = serializers.SerializerMethodField()
	class Meta:
		model = User
		fields = ["email", "password", "tokens"]


	def get_tokens(self):
		user = auth.authenticate(email=email, password=password)
		if user is not None:
			refresh = RefreshToken.for_user(self)
			return {
				"access":str(refresh.access_token)
			}
		else:
			raise AuthenticationFailed("Incorrect Credentials!")


