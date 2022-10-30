from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from utils import upload_function


class MediaType(models.Model):
    """Формат носителя"""

    name = models.CharField(max_length=100, verbose_name='Тип носителя')

    def __str__(self):
        return f"{self.pk} | {self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(MediaType, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Тип носителя'
        verbose_name_plural = 'Тип носителей'


class Frontman(models.Model):
    """Артист(как отдельная личность)"""

    name = models.CharField(max_length=255, verbose_name='Фронтмен')
    slug = models.SlugField(editable=False)
    image = models.ImageField(upload_to=upload_function, null=True, blank=True)

    def __str__(self):
        return f"{self.pk} | {self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Frontman, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Фронтмен'
        verbose_name_plural = 'Фронтмены'


class Genre(models.Model):
    """Жанр музыки"""

    name = models.CharField(max_length=50, verbose_name='Название жанра')
    slug = models.SlugField(editable=False)

    def __str__(self):
        return f"{self.pk} | {self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Artist(models.Model):
    """Группа"""

    name = models.CharField(max_length=255, verbose_name='Исполнитель')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Жанр")
    frontman = models.ForeignKey(Frontman, on_delete=models.CASCADE, verbose_name="Фронтмен")
    slug = models.SlugField(editable=False)
    image = models.ImageField(upload_to=upload_function, null=True, blank=True)

    def __str__(self):
        return f'{self.pk} | {self.name} | {self.genre.name}| {self.image}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('artist_detail', kwargs={'artist_slug': self.slug})

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Album(models.Model):
    """Альбом"""

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='Исполнитель')
    name = models.CharField(max_length=255, verbose_name='Название альбома')
    media_type = models.ForeignKey(MediaType, verbose_name='Носитель', on_delete=models.CASCADE)
    release_date = models.DateField(verbose_name='Дата релиза')
    slug = models.SlugField(editable=False)
    description = models.TextField(verbose_name='Описание', default='Описание отсутствует')
    stock = models.IntegerField(default=1, verbose_name='Наличие')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    offer_of_the_week = models.BooleanField(default=False, verbose_name='Предложение недели?')
    image = models.ImageField(upload_to=upload_function, null=True, blank=True)
    track = models.FileField(null=True, blank=True, verbose_name='Демо-трек', upload_to=upload_function)

    def __str__(self):
        return f'{self.pk} | {self.artist.name} | {self.name} | {self.release_date}'

    def get_absolute_url(self):
        return reverse('album_detail', kwargs={'artist_slug': self.artist.slug, 'album_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Album, self).save(*args, **kwargs)

    def ct_model(self):
        return self._meta.model_name

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = 'Альбомы'
