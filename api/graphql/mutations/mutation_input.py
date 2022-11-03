import graphene
from graphene_file_upload.scalars import Upload


class MediaTypeCreateInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)


class MediaTypeUpdateInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class FrontmanCreateInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    image = Upload()


class FrontmanUpdateInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    image = Upload()


class GenreCreateInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)


class GenreUpdateInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class ArtistCreateInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    frontman = FrontmanCreateInput(required=True)
    genre = GenreCreateInput(required=True)
    image = Upload()


class ArtistUpdateInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    frontman = FrontmanUpdateInput()
    genre = GenreUpdateInput()
    image = Upload()


class AlbumCreateInput(graphene.InputObjectType):
    id = graphene.ID()
    artist = ArtistCreateInput(required=True)
    name = graphene.String(required=True)
    media_type = MediaTypeCreateInput(required=True)
    release_date = graphene.Date(required=True)
    description = graphene.String(required=True)
    stock = graphene.Int(required=True)
    price = graphene.Decimal(required=True)
    offer_of_the_week = graphene.Boolean(required=True)
    image = Upload()
    track = Upload()


class AlbumUpdateInput(graphene.InputObjectType):
    id = graphene.ID()
    artist = ArtistUpdateInput()
    name = graphene.String()
    media_type = MediaTypeUpdateInput()
    release_date = graphene.Date()
    description = graphene.String()
    stock = graphene.Int()
    price = graphene.Decimal()
    offer_of_the_week = graphene.Boolean()
    image = Upload()
    track = Upload()
