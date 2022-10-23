from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


# class ArtistInline(admin.TabularInline):
#     model = Artist.frontman.through
#
#
# class FrontmanAdmin(admin.ModelAdmin):
#     model = Frontman
#     readonly_fields = ('slug',)
#     inlines = [
#         ArtistInline,
#     ]


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

    # class ArtistAdmin(admin.ModelAdmin):
    #     readonly_fields = ('slug',)
    #     inlines = [
    #         ArtistInline,
    #     ]
    #     exclude = ('frontman',)


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
