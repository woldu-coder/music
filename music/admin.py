from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
	fieldsets = (
			("User Name", {
				"fields": ("first_name", "last_name", "username", "phone_number", "email", "profile_picture", "password")
				}),
			("Permissions", {
				"fields":("user_permissions", "groups", "is_staff", "is_superuser")
				})
		)
admin.site.register(User)

class BlogAdminArea(admin.AdminSite):
	site_header = "Music Control Admin Site"
	site_title = "Music Band"

music_admin = BlogAdminArea(name="Music Admin Area")

class UserForStaffs(admin.ModelAdmin):
	list_display = ("first_name", "last_name", "username", "email", "phone_number")
	list_filter  = ("first_name", "email", "phone_number")
	search_fields = ("is_staff", "is_superuser")
	list_display_links = ("first_name", "email")

class ArtistAdmin(admin.ModelAdmin):
	list_display = ("artist_name", "artist_phone", "address")
	search_fields = ("artist_name", "artist_phone", "address")
	list_filter = ("artist_name", "artist_phone", "address")

music_admin.register(Artist, ArtistAdmin)

class AlbumAdmin(admin.ModelAdmin):
	list_display  = ("album_name", "artist")
	search_fields = ("album_name", "artist")
	list_filter = ("album_name", "artist")

class GenreAdmin(admin.ModelAdmin):
	list_display = ("genre", )

class MusictypeAdmin(admin.ModelAdmin):
	list_display = ("music_type", )

class MusicAdmin(admin.ModelAdmin):
	list_display = ("music_name", "artist", "album")
	search_fields = ("music_name", "artist", "album")
	list_filter = ("music_name", "artist", "album")

music_admin.register(Music, MusicAdmin)
music_admin.register(MusicType, MusictypeAdmin)
music_admin.register(Album, AlbumAdmin)
music_admin.register(Genre, GenreAdmin)
music_admin.register(User, UserForStaffs)
