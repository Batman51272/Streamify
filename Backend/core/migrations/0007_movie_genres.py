# Generated by Django 5.1.3 on 2024-12-01 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_comment_movie_id_remove_comment_post_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
