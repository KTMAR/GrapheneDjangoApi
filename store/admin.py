from django.contrib import admin
from .models import *


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


class GenreAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


class ArtistAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


class FrontmanAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


admin.site.register(Genre, GenreAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Frontman, FrontmanAdmin)
admin.site.register(MediaType)
