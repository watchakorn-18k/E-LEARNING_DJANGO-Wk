# Generated by Django 3.2.4 on 2021-07-01 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyWebsite', '0012_auto_20210702_0544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter_field_m4',
            name='verfify_score',
        ),
    ]
