import graphene
from store.models import \
    Genre, \
    Frontman, \
    Artist, \
    MediaType, \
    Album


class DeleteMixin:
    class Arguments:
        id = graphene.ID()

    ok = graphene.Boolean()


class DeleteMediaType(graphene.Mutation, DeleteMixin):

    @classmethod
    def mutate(cls, root, info, **kwargs):
        obj = MediaType.objects.get(pk=kwargs["id"])
        obj.delete()
        return cls(
            ok=True,
        )


class DeleteFrontman(graphene.Mutation, DeleteMixin):

    @classmethod
    def mutate(cls, root, info, **kwargs):
        obj = Frontman.objects.get(pk=kwargs["id"])
        obj.delete()
        return cls(
            ok=True,
        )


class DeleteGenre(graphene.Mutation, DeleteMixin):

    @classmethod
    def mutate(cls, root, info, **kwargs):
        obj = Genre.objects.get(pk=kwargs["id"])
        obj.delete()
        return cls(
            ok=True,
        )


class DeleteArtist(graphene.Mutation, DeleteMixin):

    @classmethod
    def mutate(cls, root, info, **kwargs):
        obj = Artist.objects.get(pk=kwargs["id"])
        obj.delete()
        return cls(
            ok=True,
        )


class DeleteAlbum(graphene.Mutation, DeleteMixin):

    @classmethod
    def mutate(cls, root, info, **kwargs):
        obj = Album.objects.get(pk=kwargs["id"])
        obj.delete()
        return cls(
            ok=True,
        )
