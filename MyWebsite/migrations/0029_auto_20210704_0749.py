# Generated by Django 3.2.4 on 2021-07-04 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWebsite', '0028_auto_20210704_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='technology_student_name_m_5',
            name='name_work_2',
            field=models.CharField(default='2', max_length=110, verbose_name='ใบงานที่'),
        ),
        migrations.AddField(
            model_name='technology_student_name_m_5',
            name='name_work_3',
            field=models.CharField(default='3', max_length=110, verbose_name='ใบงานที่'),
        ),
        migrations.AddField(
            model_name='technology_student_name_m_5',
            name='name_work_4',
            field=models.CharField(default='4', max_length=110, verbose_name='ใบงานที่'),
        ),
        migrations.AddField(
            model_name='technology_student_name_m_5',
            name='name_work_5',
            field=models.CharField(default='5', max_length=110, verbose_name='ใบงานที่'),
        ),
        migrations.AddField(
            model_name='technology_student_name_m_5',
            name='name_work_6',
            field=models.CharField(default='6', max_length=110, verbose_name='ใบงานที่'),
        ),
        migrations.AddField(
            model_name='technology_student_name_m_5',
            name='name_work_7',
            field=models.CharField(default='7', max_length=110, verbose_name='ใบงานที่'),
        ),
        migrations.AddField(
            model_name='technology_student_name_m_5',
            name='name_work_8',
            field=models.CharField(default='8', max_length=110, verbose_name='ใบงานที่'),
        ),
        migrations.AddField(
            model_name='technology_student_name_m_5',
            name='name_work_9',
            field=models.CharField(default='9', max_length=110, verbose_name='ใบงานที่'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_1',
            field=models.IntegerField(default='0', max_length=110, verbose_name='คะแนนที่ 1'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_2',
            field=models.IntegerField(default='0', max_length=110, verbose_name='คะแนนที่ 2'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_3',
            field=models.IntegerField(default='0', max_length=110, verbose_name='คะแนนที่ 3'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='work_success_student_1',
            field=models.CharField(default='0', max_length=110, verbose_name='ผลงานที่เสร็จ 1'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='work_success_student_2',
            field=models.CharField(default='0', max_length=110, verbose_name='ผลงานที่เสร็จ 2'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='work_success_student_3',
            field=models.CharField(default='0', max_length=110, verbose_name='ผลงานที่เสร็จ 3'),
        ),
    ]
