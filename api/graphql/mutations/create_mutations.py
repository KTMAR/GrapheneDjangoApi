import graphene
from .mutation_input import FrontmanInput, GenreInput, ArtistInput, AlbumInput, MediaTypeInput
from ..query_types import FrontmanType, ArtistType, GenreType, AlbumType, MediaTypeType
from store.models import Genre, Frontman, Artist, MediaType, Album


class CreateMediaType(graphene.Mutation):
    class Arguments:
        media_type_data = MediaTypeInput(required=True)

    media_type = graphene.Field(MediaTypeType)

    @staticmethod
    def mutate(self, info, media_type_data):
        media_type, status = MediaType.objects.get_or_create(name=media_type_data.name)
        return CreateMediaType(
            media_type=media_type,
        )


class CreateFrontman(graphene.Mutation):
    class Arguments:
        frontman_data = FrontmanInput(required=True)

    frontman = graphene.Field(FrontmanType)

    @staticmethod
    def mutate(self, info, frontman_data=None):
        frontman, status = Frontman.objects.get_or_create(name=frontman_data.name)
        return CreateFrontman(
            frontman=frontman,
        )


class CreateGenre(graphene.Mutation):
    class Arguments:
        genre_data = GenreInput(required=True)

    genre = graphene.Field(GenreType)

    @staticmethod
    def mutate(self, info, genre_data=None):
        genre, status = Genre.objects.get_or_create(name=genre_data.name)
        return CreateGenre(
            genre=genre,
        )


class CreateArtist(graphene.Mutation):
    class Arguments:
        input_data = ArtistInput(required=True, name="input")

    artist = graphene.Field(ArtistType, required=True)

    @staticmethod
    def mutate(root, info, input_data):
        genre, created = Genre.objects.get_or_create(name=input_data.genre.name)
        frontman, created = Frontman.objects.get_or_create(name=input_data.frontman.name)

        artist, created = Artist.objects.get_or_create(
            name=input_data.name,
            genre=genre,
            frontman=frontman)

        return CreateArtist(artist=artist)


class CreateAlbum(graphene.Mutation):
    class Arguments:
        input_data = AlbumInput(required=True, name="input")

    album = graphene.Field(AlbumType, required=True)

    @staticmethod
    def mutate(root, info, input_data):
        media_type = MediaType.objects.get_or_create(name=input_data.media_type.name)
        genre, created = Genre.objects.get_or_create(name=input_data.artist.genre.name)
        frontman, created = Frontman.objects.get_or_create(name=input_data.artist.frontman.name)

        artist = Artist.objects.get_or_create(
            name=input_data.artist.name,
            genre=genre,
            frontman=frontman
        )

        album = Album.objects.get_or_create(
            name=input_data.name,
            artist=artist,
            media_type=media_type,
            release_date=input_data.release_date,
            description=input_data.description,
            stock=input_data.stock,
            price=input_data.price,
            offer_of_the_week=input_data.offer_of_the_week,
        )

        return CreateAlbum(album=album)
