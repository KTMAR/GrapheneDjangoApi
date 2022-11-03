import graphene
from .mutation_input import MediaTypeCreateInput, FrontmanCreateInput, GenreCreateInput, ArtistCreateInput, \
    AlbumCreateInput, \
    AlbumUpdateInput, \
    FrontmanUpdateInput, GenreUpdateInput, ArtistUpdateInput
from ..query_types import MediaTypeType, FrontmanType, GenreType, ArtistType, AlbumType
from store.models import MediaType, Frontman, Genre, Artist, Album


class UpdateMediaType(graphene.Mutation):
    class Arguments:
        media_type_data = MediaTypeCreateInput(required=True, name="input")

    media_type = graphene.Field(MediaTypeType)

    @staticmethod
    def mutate(self, info, media_type_data):
        try:
            media_type_obj = MediaType.objects.get(pk=media_type_data.id)
        except MediaType.DoesNotExist:
            pass
        else:
            media_type_obj.name = media_type_data.name
            media_type_obj.save()

        return UpdateMediaType(
            media_type=media_type_obj,
        )


class UpdateFrontman(graphene.Mutation):
    class Arguments:
        frontman_data = FrontmanUpdateInput(name="input")

    frontman = graphene.Field(FrontmanType)

    @staticmethod
    def mutate(self, info, frontman_data):
        try:
            frontman_obj = Frontman.objects.get(pk=frontman_data.id)
        except Frontman.DoesNotExist:
            pass
        else:
            if frontman_data.image:
                frontman_obj.image.delete()
                frontman_obj.image = frontman_data.image

            frontman_obj.save()

        return UpdateFrontman(
            frontman=frontman_obj,
        )


class UpdateGenre(graphene.Mutation):
    class Arguments:
        genre_data = GenreUpdateInput(name="input")

    genre = graphene.Field(GenreType)

    @staticmethod
    def mutate(self, info, genre_data):
        try:
            genre_obj = Genre.objects.get(pk=genre_data.id)
        except Genre.DoesNotExist:
            pass
        else:
            genre_obj.name = genre_data.name
        genre_obj.save()

        return UpdateGenre(
            genre=genre_obj,
        )


class UpdateArtist(graphene.Mutation):
    class Arguments:
        artist_data = ArtistUpdateInput(name="input")

    artist = graphene.Field(ArtistType)

    @staticmethod
    def mutate(self, info, artist_data):

        try:
            artist_obj = Artist.objects.get(pk=artist_data.id)
        except Artist.DoesNotExist:
            return None
        else:

            if artist_data.name:
                artist_obj.name = artist_data.name

            if artist_data.frontman:
                try:
                    frontman_obj = Frontman.objects.get(pk=artist_data.frontman.id)
                except Frontman.DoesNotExist:
                    pass
                else:
                    frontman_obj.image = artist_data.frontman.image
                    artist_obj.frontman_id = frontman_obj.pk

            if artist_data.genre:
                try:
                    genre_obj = Genre.objects.get(pk=artist_data.genre.id)
                except Genre.DoesNotExist:
                    pass
                else:
                    artist_obj.genre_id = genre_obj.pk

            if artist_data.image:
                artist_obj.image.delete()
                artist_obj.image = artist_data.image

            artist_obj.save()

        return UpdateArtist(
            artist=artist_obj,
        )


class UpdateAlbum(graphene.Mutation):
    class Arguments:
        album_data = AlbumUpdateInput(name="input")

    album = graphene.Field(AlbumType)

    @staticmethod
    def mutate(self, info, album_data):

        try:
            album_obj = Album.objects.get(pk=album_data.id)
        except Album.DoesNotExist:
            return None
        else:
            if album_data.artist:
                try:
                    artist_obj = Artist.objects.get(
                        pk=album_data.artist.id
                    )
                except Artist.DoesNotExist:
                    return None
                else:
                    if album_data.artist.frontman:
                        try:
                            frontman_obj = Frontman.objects.get(pk=album_data.artist.frontman.id)
                        except Frontman.DoesNotExist:
                            pass
                        else:
                            artist_obj.frontman_id = frontman_obj.pk
                    if album_data.artist.genre:
                        try:
                            genre_obj = Genre.objects.get(pk=album_data.artist.genre.id)
                        except Genre.DoesNotExist:
                            pass
                        else:
                            artist_obj.genre_id = genre_obj.pk

                    artist_obj.save()
                    album_obj.artist_id = artist_obj.pk

        if album_data.media_type:
            try:
                media_type_obj = MediaType.objects.get(pk=album_data.media_type.id)
            except MediaType.DoesNotExist:
                pass
            else:
                album_obj.media_type_id = media_type_obj.pk

        if album_data.name:
            album_obj.name = album_data.name

        if album_data.description:
            album_obj.description = album_data.description

        if album_data.stock:
            album_obj.stock = album_data.stock

        if album_data.price:
            album_obj.price = album_data.price

        if album_data.offer_of_the_week:
            album_obj.offer_of_the_week = album_data.offer_of_the_week

        if album_data.release_date:
            album_obj.release_date = album_data.release_date

        if album_data.image:
            album_obj.image.delete()
            album_obj.image = album_data.image

        if album_data.track:
            album_obj.track.delete()
            album_obj.track = album_data.track

        album_obj.save()

        return UpdateAlbum(
            album=album_obj,
        )
