# Generated by Django 2.2.6 on 2019-11-23 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_place_visitors'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='ext_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='Внешинй ID'),
        ),
        migrations.AddField(
            model_name='place',
            name='image_link',
            field=models.URLField(blank=True, verbose_name='ссылка на картинку'),
        ),
        migrations.AddField(
            model_name='place',
            name='source',
            field=models.CharField(choices=[('DH-CENTER', 'DH-CENTER'), ('DH-CENTER', 'LitMap')], default='LitMap', max_length=12),
        ),
        migrations.AddField(
            model_name='place',
            name='wiki_link',
            field=models.URLField(blank=True, verbose_name='Ссылка на wiki'),
        ),
    ]