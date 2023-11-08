# Generated by Django 4.0 on 2023-11-08 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('place_id', models.CharField(max_length=50, verbose_name='id')),
                ('description_short', models.TextField(verbose_name='Краткое описание')),
                ('description_long', models.TextField(verbose_name='Описание')),
                ('lng_coordinates', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Долгота')),
                ('lat_coordinates', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Ширина')),
            ],
        ),
        migrations.CreateModel(
            name='PlaceImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='place_img', verbose_name='Фото места')),
            ],
        ),
    ]
