# Generated by Django 3.2.4 on 2021-07-04 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWebsite', '0029_auto_20210704_0749'),
    ]

    operations = [
        migrations.CreateModel(
            name='SBMLD_Chapter_content_m6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_id', models.CharField(max_length=110, verbose_name='บทที่')),
                ('chapter_name', models.CharField(max_length=1500, verbose_name='ชื่อบท')),
                ('content', models.CharField(max_length=1500, verbose_name='ลิงก์เนื้อหา iframe')),
                ('textwork', models.CharField(max_length=1500, verbose_name='อธิบายใบงาน')),
                ('work', models.CharField(max_length=1500, verbose_name='ลิงก์ใบงาน รูปภาพ')),
                ('content_video', models.CharField(default='0', max_length=1500, verbose_name='ลิงก์เนื้อหา วิดีโอ')),
                ('lasttime', models.CharField(max_length=1500, verbose_name='ระยะเวลา')),
            ],
            options={
                'verbose_name_plural': 'เนื้อหาวิชาเทคโนโลยี ม.5',
            },
        ),
        migrations.CreateModel(
            name='SBMLD_Student_name_m_6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=1500, verbose_name='ชื่อจริง')),
                ('last_name', models.CharField(max_length=1500, verbose_name='นามสกุล')),
                ('name_work_1', models.CharField(default='1', max_length=110, verbose_name='ใบงานที่ 1')),
                ('score_1', models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 1')),
                ('work_success_student_1', models.CharField(default='0', max_length=110, verbose_name='ผลงานที่เสร็จ 1')),
                ('name_work_2', models.CharField(default='2', max_length=110, verbose_name='ใบงานที่ 2')),
                ('score_2', models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 2')),
                ('work_success_student_2', models.CharField(default='0', max_length=110, verbose_name='ผลงานที่เสร็จ 2')),
                ('name_work_3', models.CharField(default='3', max_length=110, verbose_name='ใบงานที่ 3')),
                ('score_3', models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 3')),
                ('work_success_student_3', models.CharField(default='0', max_length=110, verbose_name='ผลงานที่เสร็จ 3')),
                ('name_work_4', models.CharField(default='4', max_length=110, verbose_name='ใบงานที่ 4')),
                ('score_4', models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 4')),
                ('work_success_student_4', models.CharField(default='0', max_length=110, verbose_name='ผลงานที่เสร็จ 4')),
                ('name_work_5', models.CharField(default='5', max_length=110, verbose_name='ใบงานที่ 5')),
                ('score_5', models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 5')),
                ('work_success_student_5', models.CharField(default='0', max_length=110, verbose_name='ผลงานที่เสร็จ 5')),
                ('name_work_6', models.CharField(default='6', max_length=110, verbose_name='ใบงานที่ 6')),
                ('score_6', models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 6')),
                ('work_success_student_6', models.CharField(default='0', max_length=110, verbose_name='ผลงานที่เสร็จ 6')),
                ('name_work_7', models.CharField(default='7', max_length=110, verbose_name='ใบงานที่ 7')),
                ('score_7', models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 7')),
                ('work_success_student_7', models.CharField(default='0', max_length=110, verbose_name='ผลงานที่เสร็จ 7')),
                ('name_work_8', models.CharField(default='8', max_length=110, verbose_name='ใบงานที่ 8')),
                ('score_8', models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 8')),
                ('work_success_student_8', models.CharField(default='0', max_length=110, verbose_name='ผลงานที่เสร็จ 8')),
                ('name_work_9', models.CharField(default='9', max_length=110, verbose_name='ใบงานที่ 9')),
                ('score_9', models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 9')),
                ('work_success_student_9', models.CharField(default='0', max_length=110, verbose_name='ผลงานที่เสร็จ 9')),
            ],
            options={
                'verbose_name_plural': 'รายชื่อนักเรียนวิชาเทคโนโลยี ม.5',
            },
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_1',
            field=models.CharField(default='1', max_length=110, verbose_name='ใบงานที่ 1'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_2',
            field=models.CharField(default='2', max_length=110, verbose_name='ใบงานที่ 2'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_3',
            field=models.CharField(default='3', max_length=110, verbose_name='ใบงานที่ 3'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_4',
            field=models.CharField(default='4', max_length=110, verbose_name='ใบงานที่ 4'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_5',
            field=models.CharField(default='5', max_length=110, verbose_name='ใบงานที่ 5'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_6',
            field=models.CharField(default='6', max_length=110, verbose_name='ใบงานที่ 6'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_7',
            field=models.CharField(default='7', max_length=110, verbose_name='ใบงานที่ 7'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_8',
            field=models.CharField(default='8', max_length=110, verbose_name='ใบงานที่ 8'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_9',
            field=models.CharField(default='9', max_length=110, verbose_name='ใบงานที่ 9'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_1',
            field=models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 1'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_2',
            field=models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 2'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_3',
            field=models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 3'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_4',
            field=models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 4'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_5',
            field=models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 5'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_6',
            field=models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 6'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_7',
            field=models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 7'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_8',
            field=models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 8'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_9',
            field=models.IntegerField(default='0', max_length=110, verbose_name='คะแนนใบงานที่ 9'),
        ),
    ]
