# Generated by Django 4.1.2 on 2022-10-22 13:44

from django.db import migrations, models
import django.db.models.deletion
import utils.uploading


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Frontman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Фронтмен')),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'verbose_name': 'Фронтмен',
                'verbose_name_plural': 'Фронтмены',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название жанра')),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Тип носителя')),
            ],
            options={
                'verbose_name': 'Тип носителя',
                'verbose_name_plural': 'Тип носителей',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Исполнитель')),
                ('slug', models.SlugField(editable=False)),
                ('frontman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.frontman', verbose_name='Фронтмен')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Исполнитель',
                'verbose_name_plural': 'Исполнители',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название альбома')),
                ('release_date', models.DateField(verbose_name='Дата релиза')),
                ('slug', models.SlugField(editable=False)),
                ('description', models.TextField(default='Описание отсутствует', verbose_name='Описание')),
                ('stock', models.IntegerField(default=1, verbose_name='Наличие')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('offer_of_the_week', models.BooleanField(default=False, verbose_name='Предложение недели?')),
                ('track', models.FileField(blank=True, null=True, upload_to=utils.uploading.upload_function, verbose_name='Демо-трек')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.artist', verbose_name='Исполнитель')),
                ('media_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.mediatype', verbose_name='Носитель')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
    ]