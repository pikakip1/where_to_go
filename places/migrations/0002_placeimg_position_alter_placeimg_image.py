# Generated by Django 4.0 on 2023-11-12 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeimg',
            name='position',
            field=models.PositiveIntegerField(null=True, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='placeimg',
            name='image',
            field=models.ImageField(blank=True, upload_to='place_img', verbose_name='Фото'),
        ),
    ]
