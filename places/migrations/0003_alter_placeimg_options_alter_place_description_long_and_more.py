# Generated by Django 4.0 on 2023-11-13 09:43

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_placeimg_position_alter_placeimg_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placeimg',
            options={'ordering': ['position']},
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='placeimg',
            name='image',
            field=models.ImageField(blank=True, unique=True, upload_to='place_img', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='placeimg',
            name='position',
            field=models.PositiveIntegerField(db_index=True, default=0, null=True, verbose_name='Позиция'),
        ),
    ]