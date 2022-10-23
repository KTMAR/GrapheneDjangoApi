import graphene


class FrontmanInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class GenreInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


# class ArtistInput(graphene.InputObjectType):
#     name = graphene.String()
#     genre_id = graphene.InputField(GenreInput)
#     frontman_id = graphene.InputField(FrontmanInput)


# class AlbumInput(graphene.InputObjectType):
#     name = graphene.String()
#     genre = graphene.Field(GenreInput)
#     members = graphene.Field(MembersInput)
