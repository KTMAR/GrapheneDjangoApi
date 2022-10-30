from datetime import datetime

import graphene
from .mutation_input import MediaTypeInput, FrontmanInput, GenreInput, ArtistInput, AlbumInput
from ..query_types import MediaTypeType, FrontmanType, GenreType, ArtistType, AlbumType
from store.models import MediaType, Frontman, Genre, Artist, Album


class UpdateMediaType(graphene.Mutation):
    class Arguments:
        media_type_data = MediaTypeInput(required=True)

    media_type = graphene.Field(MediaTypeType)

    @staticmethod
    def mutate(self, info, media_type_data):
        media_type_obj = MediaType.objects.get(pk=media_type_data.id)
        media_type_obj.name = media_type_data.name
        media_type_obj.save()

        return UpdateMediaType(
            media_type=media_type_obj,
        )


class UpdateFrontman(graphene.Mutation):
    class Arguments:
        frontman_data = FrontmanInput(required=True)

    frontman = graphene.Field(FrontmanType)

    @staticmethod
    def mutate(self, info, frontman_data):
        frontman_obj = Frontman.objects.get(pk=frontman_data.id)
        frontman_obj.name = frontman_data.name
        frontman_obj.save()

        return UpdateFrontman(
            frontman=frontman_obj,
        )


class UpdateGenre(graphene.Mutation):
    class Arguments:
        genre_data = GenreInput(required=True)

    genre = graphene.Field(GenreType)

    @staticmethod
    def mutate(self, info, genre_data):
        genre_obj = Genre.objects.get(pk=genre_data.id)
        genre_obj.name = genre_data.name
        genre_obj.save()

        return UpdateGenre(
            genre=genre_obj,
        )


class UpdateArtist(graphene.Mutation):
    class Arguments:
        artist_data = ArtistInput(required=True)

    artist = graphene.Field(ArtistType)

    @staticmethod
    def mutate(self, info, artist_data):
        genre, created = Genre.objects.get_or_create(name=artist_data.genre.name)
        frontman, created = Frontman.objects.get_or_create(name=artist_data.frontman.name)

        artist_obj = Artist.objects.get(pk=artist_data.id)
        artist_obj.name = artist_data.name
        artist_obj.frontman_id = frontman.pk
        artist_obj.genre_id = genre.pk
        artist_obj.save()

        return UpdateArtist(
            artist=artist_obj,
        )


class UpdateAlbum(graphene.Mutation):
    class Arguments:
        album_data = AlbumInput(required=True)

    album = graphene.Field(AlbumType)

    @staticmethod
    def mutate(self, info, album_data):
        genre, created = Genre.objects.get_or_create(name=album_data.artist.genre.name)
        frontman, created = Frontman.objects.get_or_create(name=album_data.artist.frontman.name)
        artist, created = Artist.objects.get_or_create(
            name=album_data.artist.name,
            frontman_id=frontman.pk,
            genre_id=genre.pk)

        media_type, created = MediaType.objects.get_or_create(name=album_data.media_type.name)

        album_obj = Album.objects.get(pk=album_data.id)
        album_obj.name = album_data.name
        album_obj.description = album_data.description
        album_obj.stock = album_data.stock
        album_obj.price = album_data.price
        album_obj.offer_of_the_week = album_data.offer_of_the_week
        album_obj.artist_id = artist.pk
        album_obj.media_type_id = media_type.pk
        album_obj.release_date = album_data.release_date
        album_obj.save()

        return UpdateAlbum(
            album=album_obj,
        )
