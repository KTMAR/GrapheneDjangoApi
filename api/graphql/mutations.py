import graphene
from store.models import Artist, Album, Genre, Frontman
from .mutation_input import FrontmanInput, GenreInput
from .query_types import FrontmanType, ArtistType, GenreType


class CreateFrontman(graphene.Mutation):
    class Arguments:
        frontman_data = FrontmanInput(required=True)

    frontman = graphene.Field(FrontmanType)

    @staticmethod
    def mutate(self, info, frontman_data=None):
        frontman = Frontman.objects.create(name=frontman_data.name)
        print(frontman)
        return CreateFrontman(
            frontman=frontman
        )


class CreateGenre(graphene.Mutation):
    class Arguments:
        genre_data = GenreInput(required=True)

    genre = graphene.Field(GenreType)

    @staticmethod
    def mutate(self, info, genre_data=None):
        genre = Genre.objects.create(name=genre_data.name)
        print(genre)
        return CreateGenre(
            genre=genre
        )


class Mutation(graphene.ObjectType):
    create_member = CreateFrontman.Field()
    create_genre = CreateGenre.Field()
