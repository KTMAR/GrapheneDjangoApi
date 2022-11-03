import graphene
from .mutation_input import FrontmanCreateInput, GenreCreateInput, ArtistCreateInput, AlbumCreateInput, MediaTypeCreateInput
from ..query_types import FrontmanType, ArtistType, GenreType, AlbumType, MediaTypeType
from store.models import Genre, Frontman, Artist, MediaType, Album
from graphene_django.debug import DjangoDebug


class CreateMediaType(graphene.Mutation):
    class Arguments:
        media_type_data = MediaTypeCreateInput(required=True, name="input")

    media_type = graphene.Field(MediaTypeType)
    debug = graphene.Field(DjangoDebug, name='_debug')

    @staticmethod
    def mutate(self, info, media_type_data):
        media_type, status = MediaType.objects.get_or_create(
            name=media_type_data.name
        )
        return CreateMediaType(
            media_type=media_type,
        )


class CreateFrontman(graphene.Mutation):
    class Arguments:
        frontman_data = FrontmanCreateInput(required=True, name="input")

    frontman = graphene.Field(FrontmanType)
    debug = graphene.Field(DjangoDebug, name='_debug')

    @staticmethod
    def mutate(self, info, frontman_data=None):
        try:
            obj = Frontman.objects.get(
                name=frontman_data.name
            )
        except Frontman.DoesNotExist:
            obj = Frontman(
                name=frontman_data.name,
                image=frontman_data.image
            )
            obj.save()

        return CreateFrontman(
            frontman=obj,
        )


class CreateGenre(graphene.Mutation):
    class Arguments:
        genre_data = GenreCreateInput(required=True, name="input")

    genre = graphene.Field(GenreType)
    debug = graphene.Field(DjangoDebug, name='_debug')

    @staticmethod
    def mutate(self, info, genre_data=None):
        genre, status = Genre.objects.get_or_create(
            name=genre_data.name
        )
        return CreateGenre(
            genre=genre,
        )


class CreateArtist(graphene.Mutation):
    class Arguments:
        input_data = ArtistCreateInput(required=True, name="input")

    artist = graphene.Field(ArtistType, required=True)
    debug = graphene.Field(DjangoDebug, name='_debug')

    @staticmethod
    def mutate(root, info, input_data):

        genre, created = Genre.objects.get_or_create(
            name=input_data.genre.name
        )
        try:
            frontman = Frontman.objects.get(
                name=input_data.frontman.name
            )
        except Frontman.DoesNotExist:
            frontman = Frontman(
                name=input_data.frontman.name,
                image=input_data.frontman.image
            )
            frontman.save()

        try:
            obj = Artist.objects.get(
                name=input_data.name,
                genre=genre,
                frontman=frontman
            )
        except Artist.DoesNotExist:
            obj = Artist(
                name=input_data.name,
                genre=genre, frontman=frontman,
                image=input_data.image
            )
            obj.save()

        return CreateArtist(artist=obj)


class CreateAlbum(graphene.Mutation):
    class Arguments:
        input_data = AlbumCreateInput(required=True, name="input")

    album = graphene.Field(AlbumType, required=True)
    debug = graphene.Field(DjangoDebug, name='_debug')

    @staticmethod
    def mutate(root, info, input_data):
        media_type, created = MediaType.objects.get_or_create(
            name=input_data.media_type.name
        )
        genre, created = Genre.objects.get_or_create(
            name=input_data.artist.genre.name
        )

        try:
            frontman = Frontman.objects.get(
                name=input_data.artist.frontman.name
            )

        except Frontman.DoesNotExist:
            frontman = Frontman(
                name=input_data.artist.frontman.name,
                image=input_data.artist.frontman.image
            )
            frontman.save()

        try:
            artist = Artist.objects.get(
                name=input_data.artist.name,
                genre=genre, frontman=frontman
            )
        except Artist.DoesNotExist:
            artist = Artist(name=input_data.artist.name,
                            genre=genre, frontman=frontman,
                            image=input_data.artist.image
                            )
            artist.save()

        try:
            obj = Album.objects.get(
                name=input_data.name,
                artist_id=artist.pk,
                media_type_id=media_type.id,
                release_date=input_data.release_date,
                description=input_data.description,
                stock=input_data.stock,
                price=input_data.price,
                offer_of_the_week=input_data.offer_of_the_week
            )

        except Album.DoesNotExist:
            obj = Album(
                name=input_data.name,
                artist=artist,
                media_type=media_type,
                release_date=input_data.release_date,
                description=input_data.description,
                stock=input_data.stock,
                price=input_data.price,
                offer_of_the_week=input_data.offer_of_the_week,

            )
            obj.save()

        return CreateAlbum(album=obj)
