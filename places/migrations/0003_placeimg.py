# Generated by Django 4.0 on 2023-11-07 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_place_lat_coordinates_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='place_img', verbose_name='Фото места')),
            ],
        ),
    ]
