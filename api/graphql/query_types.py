from graphene_django import DjangoObjectType, DjangoListField
from store.models import Artist, Album, Genre, Frontman


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


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album
        fields = ("id", "slug", "artist", "name", "media_type", "release_date", "description", "stock", "price",
                  "offer_of_the_week", "track")
