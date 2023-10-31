from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
# Create your models here.
# Creating Artist
# 	- name
# 	- phone (+251) 9--------
# 	- address
# 	- number of album
# 	- total songs
# 	- 

class User(AbstractUser):
	first_name   = models.CharField(max_length=50)
	last_name 	 = models.CharField(max_length=50)
	username  	 = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=50, null=True, blank=True)

	email 	  		= models.EmailField(unique=True)
	profile_picture = models.ImageField(default="images/images/sanyii_mootii.jpg", null=True, blank=True, upload_to="profile/%Y/%m/%d")
	created_at 		= models.DateTimeField(auto_now_add=True, null=True, blank=True)
	password 		= models.CharField(max_length=100, null=True, blank=True)
	token 			= models.CharField(max_length=500, null=True, blank=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ["first_name", "last_name", "username", "phone_number"]

	def __str__(self):
		return self.first_name+ " "+self.last_name




class Artist(models.Model):
	artist_name = models.CharField(max_length=200, help_text="Artist's Full Name")
	artist_phone = models.CharField(max_length=15, null=True, blank=True)
	address = models.CharField(max_length=200, help_text="Address of Artist")
	#
	# You can add many more about artist like
	#  - photo url, band, his birth place, 
	#  - when starts music, educational level
	def __str__(self):
		return self.artist_name[:20]

	class Meta:
		ordering = ["artist_name", "artist_phone", "address"]


	@property
	def album_lists(self):
		return self.album_set.all()
	
	@property
	def total_album(self):
		return self.album_set.count()
# Creating Album
# 	- album_name
# 	- band
# 	- artist
# 	- 
class Album(models.Model):
	album_name = models.CharField(max_length=200)
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
	avatar = CloudinaryField("images", blank=True, null=True)

	def __str__(self):
		return self.album_name

	class Meta:
		ordering = ["album_name", "artist"]

	@property
	def musics_list(self):
		return self.music_set.all()

	@property
	def total_music(self):
		return self.music_set.count()

	@property
	def artist_name(self):
		return self.artist.artist_name

	@property
	def imageURL(self):
		try:
			url = self.avatar.url
		except:
			url = ""
		return url


# Genre
# 	- genres_type

class Genre(models.Model):
	genre = models.CharField(max_length=50)

	def __str__(self):
		return self.genre

	class Meta:
		ordering = ["genre",]

# Music
# 	- music_name
# 	- artist_name (Singer name)
# 	- album_name
# 	- genre
# 	- written_by
# 	- sounded_by
class MusicType(models.Model):
	music_type = models.CharField(max_length=50)

	def __str__(self):
		return self.music_type

class Music(models.Model):
	music_name = models.CharField(max_length=50)
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
	music_type = models.ForeignKey(MusicType, on_delete=models.CASCADE)
	edited_by = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.music_name

	class Meta:
		ordering = ["music_name", "artist", "album"]

	@property
	def artist_name(self):
		return self.artist.artist_name

	@property
	def album_name(self):
		return self.album.album_name

	@property
	def genre_type(self):
		return self.genre.genre

	@property
	def musics_type(self):
		return self.music_type.music_type
# Title
# Artist
# Album
# Genre
