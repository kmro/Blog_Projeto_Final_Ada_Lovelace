# Generated by Django 5.0.3 on 2024-04-06 23:40

import embed_video.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_blogpost_id_alter_comment_id_alter_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=1),
            preserve_default=False,
        ),
    ]
