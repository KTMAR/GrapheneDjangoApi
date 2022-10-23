import graphene
from .query_types import *


class Query(graphene.ObjectType):
    # Album-query start /////////////
    all_albums = graphene.List(AlbumType)
    album_by_name = graphene.Field(AlbumType, name=graphene.String(required=True))

    @staticmethod
    def resolve_all_albums(root, info):
        return Album.objects.all()

    @staticmethod
    def resolve_album_by_name(root, info, name):
        try:
            return Album.objects.get(name=name)
        except Album.DoesNotExist:
            return None

    # Album-query end /////////////

    # Artist-query start ////////
    all_artist = graphene.List(ArtistType)
    artist_by_name = graphene.Field(ArtistType, name=graphene.String(required=True))

    @staticmethod
    def resolve_all_artist(root, info):
        return Artist.objects.all()

    @staticmethod
    def resolve_artist_by_name(root, info, name):
        try:
            return Artist.objects.get(name=name)
        except Artist.DoesNotExist:
            return None

    # Artist-query end //////////

    # Frontman-query start ////////
    all_frontman = graphene.List(FrontmanType)
    frontman_by_name = graphene.Field(FrontmanType, name=graphene.String(required=True))

    @staticmethod
    def resolve_all_frontman(root, info):
        return Frontman.objects.all()

    @staticmethod
    def resolve_frontman_by_name(root, info, name):
        try:
            return Frontman.objects.get(name=name)
        except Frontman.DoesNotExist:
            return None

    # Frontman-query end ////////
    all_genre = graphene.List(GenreType)
    genre_by_name = graphene.Field(GenreType, name=graphene.String(required=True))

    @staticmethod
    def resolve_all_genre(root, info):
        return Genre.objects.all()

    @staticmethod
    def resolve_genre_by_name(root, info, name):
        try:
            return Genre.objects.get(name=name)
        except Genre.DoesNotExist:
            return None
