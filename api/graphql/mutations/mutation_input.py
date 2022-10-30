import graphene


class MediaTypeInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)


class FrontmanInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)


class GenreInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)


class ArtistInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    frontman = FrontmanInput(required=True)
    genre = GenreInput(required=True)


class AlbumInput(graphene.InputObjectType):
    id = graphene.ID()
    artist = ArtistInput(required=True)
    name = graphene.String(required=True)
    media_type = MediaTypeInput(required=True)
    release_date = graphene.Date(required=True)
    description = graphene.String(required=True)
    stock = graphene.Int(required=True)
    price = graphene.Decimal(required=True)
    offer_of_the_week = graphene.Boolean(required=True)

