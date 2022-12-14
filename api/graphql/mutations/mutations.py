import graphene
from .create_mutations import \
    CreateMediaType, \
    CreateAlbum, \
    CreateFrontman, \
    CreateGenre, \
    CreateArtist,\
    CreateUser
from .update_mutations import \
    UpdateMediaType, \
    UpdateFrontman, UpdateGenre, UpdateArtist, UpdateAlbum
from .delete_mutations import \
    DeleteMediaType, DeleteFrontman, DeleteGenre, DeleteArtist
import graphql_jwt


class Mutation(graphene.ObjectType):
    # User
    create_user = CreateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    # MediaType
    create_media_type = CreateMediaType.Field()
    update_media_type = UpdateMediaType.Field()
    delete_media_type = DeleteMediaType.Field()

    # Frontman
    create_frontman = CreateFrontman.Field()
    update_frontman = UpdateFrontman.Field()
    delete_frontman = DeleteFrontman.Field()

    # Genre
    create_genre = CreateGenre.Field()
    update_genre = UpdateGenre.Field()
    delete_genre = DeleteGenre.Field()

    # Artist
    create_artist = CreateArtist.Field()
    update_artist = UpdateArtist.Field()
    delete_artist = DeleteArtist.Field()

    # Album
    create_album = CreateAlbum.Field()
    update_album = UpdateAlbum.Field()


