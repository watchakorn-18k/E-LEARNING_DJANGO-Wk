# Generated by Django 3.2.4 on 2021-07-23 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWebsite', '0042_auto_20210704_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design_student_name_m_5',
            name='score_5',
            field=models.IntegerField(default='0', verbose_name='คะแนนที่ 5.1'),
        ),
        migrations.AlterField(
            model_name='design_student_name_m_5',
            name='score_6',
            field=models.IntegerField(default='0', verbose_name='คะแนนที่ 5.2'),
        ),
    ]