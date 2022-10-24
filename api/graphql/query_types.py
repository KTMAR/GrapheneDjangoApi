from graphene_django import DjangoObjectType
from store.models import Artist, Album, Genre, Frontman, MediaType


class MediaTypeType(DjangoObjectType):
    class Meta:
        model = MediaType
        fields = ("id", "name")


class GenreType(DjangoObjectType):
    class Meta:
        model = Genre
        fields = ("id", "name", "slug")


class FrontmanType(DjangoObjectType):
    class Meta:
        model = Frontman
        fields = ("id", "name", "slug")


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist
        fields = ("id", "name", "slug", "genre", "frontman")


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album
        fields = (
            "id", "slug", "artist", "name", "media_type", "description", "stock", "price", "offer_of_the_week",
            "release_date"
        )
