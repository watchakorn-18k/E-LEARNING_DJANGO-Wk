# Generated by Django 3.2.4 on 2021-07-01 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWebsite', '0011_chapter_content_m4_chapter_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter_field_m4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_sub', models.CharField(max_length=1500)),
                ('chapter_name', models.CharField(max_length=1500)),
                ('verfify_score', models.CharField(max_length=1500)),
            ],
        ),
        migrations.DeleteModel(
            name='Chapter_field',
        ),
    ]
