# Generated by Django 3.2.4 on 2021-07-01 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWebsite', '0015_auto_20210702_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter_content_m4',
            name='lasttime',
            field=models.CharField(default=-1.0, max_length=1500),
            preserve_default=False,
        ),
    ]
