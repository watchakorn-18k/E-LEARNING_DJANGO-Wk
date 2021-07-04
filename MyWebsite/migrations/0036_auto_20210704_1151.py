# Generated by Django 3.2.4 on 2021-07-04 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWebsite', '0035_alter_sbmld_chapter_content_m6_chapter_id_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter_content_m4',
            name='chapter_id',
            field=models.CharField(max_length=2000, verbose_name='บทที่'),
        ),
        migrations.AlterField(
            model_name='chapter_content_m4',
            name='chapter_name',
            field=models.CharField(max_length=2000, verbose_name='ชื่อบท'),
        ),
        migrations.AlterField(
            model_name='chapter_content_m4',
            name='content',
            field=models.CharField(max_length=2000, verbose_name='ลิงก์เนื้อหา iframe'),
        ),
        migrations.AlterField(
            model_name='chapter_content_m4',
            name='content_video',
            field=models.CharField(default='0', max_length=2000, verbose_name='ลิงก์เนื้อหา วิดีโอ'),
        ),
        migrations.AlterField(
            model_name='chapter_content_m4',
            name='lasttime',
            field=models.CharField(max_length=2000, verbose_name='ระยะเวลา'),
        ),
        migrations.AlterField(
            model_name='chapter_content_m4',
            name='work',
            field=models.CharField(max_length=2000, verbose_name='ลิงก์ใบงาน รูปภาพ'),
        ),
        migrations.AlterField(
            model_name='design_chapter_content_m5',
            name='chapter_id',
            field=models.CharField(max_length=2000, verbose_name='บทที่'),
        ),
        migrations.AlterField(
            model_name='design_chapter_content_m5',
            name='chapter_name',
            field=models.CharField(max_length=2000, verbose_name='ชื่อบท'),
        ),
        migrations.AlterField(
            model_name='design_chapter_content_m5',
            name='content',
            field=models.CharField(max_length=2000, verbose_name='ลิงก์เนื้อหา iframe'),
        ),
        migrations.AlterField(
            model_name='design_chapter_content_m5',
            name='content_video',
            field=models.CharField(default='0', max_length=2000, verbose_name='ลิงก์เนื้อหา วิดีโอ'),
        ),
        migrations.AlterField(
            model_name='design_chapter_content_m5',
            name='lasttime',
            field=models.CharField(max_length=2000, verbose_name='ระยะเวลา'),
        ),
        migrations.AlterField(
            model_name='design_chapter_content_m5',
            name='work',
            field=models.CharField(max_length=2000, verbose_name='ลิงก์ใบงาน รูปภาพ'),
        ),
        migrations.AlterField(
            model_name='design_student_name_m_5',
            name='first_name',
            field=models.CharField(max_length=2000, verbose_name='ชื่อจริง'),
        ),
        migrations.AlterField(
            model_name='design_student_name_m_5',
            name='last_name',
            field=models.CharField(max_length=2000, verbose_name='นามสกุล'),
        ),
        migrations.AlterField(
            model_name='design_student_name_m_5',
            name='score_1',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 1'),
        ),
        migrations.AlterField(
            model_name='design_student_name_m_5',
            name='score_2',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 2'),
        ),
        migrations.AlterField(
            model_name='design_student_name_m_5',
            name='score_3',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 3'),
        ),
        migrations.AlterField(
            model_name='design_student_name_m_5',
            name='score_4',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 4'),
        ),
        migrations.AlterField(
            model_name='design_student_name_m_5',
            name='score_5',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 5'),
        ),
        migrations.AlterField(
            model_name='design_student_name_m_5',
            name='score_6',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 6'),
        ),
        migrations.AlterField(
            model_name='design_student_name_m_5',
            name='score_7',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 7'),
        ),
        migrations.AlterField(
            model_name='design_student_name_m_5',
            name='score_8',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 8'),
        ),
        migrations.AlterField(
            model_name='design_student_name_m_5',
            name='score_9',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 9'),
        ),
        migrations.AlterField(
            model_name='sbmld_chapter_content_m6',
            name='chapter_id',
            field=models.CharField(max_length=2000, verbose_name='บทที่'),
        ),
        migrations.AlterField(
            model_name='sbmld_chapter_content_m6',
            name='chapter_id_work',
            field=models.CharField(max_length=2000, verbose_name='ใบงานที่'),
        ),
        migrations.AlterField(
            model_name='sbmld_chapter_content_m6',
            name='chapter_name',
            field=models.CharField(max_length=2000, verbose_name='ชื่อบท'),
        ),
        migrations.AlterField(
            model_name='sbmld_chapter_content_m6',
            name='content',
            field=models.CharField(max_length=2000, verbose_name='ลิงก์เนื้อหา iframe'),
        ),
        migrations.AlterField(
            model_name='sbmld_chapter_content_m6',
            name='content_video',
            field=models.CharField(default='0', max_length=2000, verbose_name='ลิงก์เนื้อหา วิดีโอ'),
        ),
        migrations.AlterField(
            model_name='sbmld_chapter_content_m6',
            name='example_work',
            field=models.CharField(max_length=2000, verbose_name='ลิงก์รูปตัวอย่าง'),
        ),
        migrations.AlterField(
            model_name='sbmld_chapter_content_m6',
            name='lasttime',
            field=models.CharField(max_length=2000, verbose_name='ระยะเวลา'),
        ),
        migrations.AlterField(
            model_name='sbmld_chapter_content_m6',
            name='textwork',
            field=models.CharField(max_length=2000, verbose_name='อธิบายใบงาน'),
        ),
        migrations.AlterField(
            model_name='sbmld_chapter_content_m6',
            name='work',
            field=models.CharField(max_length=2000, verbose_name='ลิงก์ใบงาน รูปภาพ'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='first_name',
            field=models.CharField(max_length=2000, verbose_name='ชื่อจริง'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='last_name',
            field=models.CharField(max_length=2000, verbose_name='นามสกุล'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='name_work_1',
            field=models.CharField(default='1', max_length=2000, verbose_name='ใบงานที่ 1'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='name_work_2',
            field=models.CharField(default='2', max_length=2000, verbose_name='ใบงานที่ 2'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='name_work_3',
            field=models.CharField(default='3', max_length=2000, verbose_name='ใบงานที่ 3'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='name_work_4',
            field=models.CharField(default='4', max_length=2000, verbose_name='ใบงานที่ 4'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='name_work_5',
            field=models.CharField(default='5', max_length=2000, verbose_name='ใบงานที่ 5'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='name_work_6',
            field=models.CharField(default='6', max_length=2000, verbose_name='ใบงานที่ 6'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='name_work_7',
            field=models.CharField(default='7', max_length=2000, verbose_name='ใบงานที่ 7'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='name_work_8',
            field=models.CharField(default='8', max_length=2000, verbose_name='ใบงานที่ 8'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='name_work_9',
            field=models.CharField(default='9', max_length=2000, verbose_name='ใบงานที่ 9'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='score_1',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 1'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='score_2',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 2'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='score_3',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 3'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='score_4',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 4'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='score_5',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 5'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='score_6',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 6'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='score_7',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 7'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='score_8',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 8'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='score_9',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 9'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='work_success_student_1',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 1'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='work_success_student_2',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 2'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='work_success_student_3',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 3'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='work_success_student_4',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 4'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='work_success_student_5',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 5'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='work_success_student_6',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 6'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='work_success_student_7',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 7'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='work_success_student_8',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 8'),
        ),
        migrations.AlterField(
            model_name='sbmld_student_name_m_6',
            name='work_success_student_9',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 9'),
        ),
        migrations.AlterField(
            model_name='student_name_m_4',
            name='first_name',
            field=models.CharField(max_length=2000, verbose_name='ชื่อจริง'),
        ),
        migrations.AlterField(
            model_name='student_name_m_4',
            name='last_name',
            field=models.CharField(max_length=2000, verbose_name='นามสกุล'),
        ),
        migrations.AlterField(
            model_name='student_name_m_4',
            name='score_1',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 1'),
        ),
        migrations.AlterField(
            model_name='student_name_m_4',
            name='score_2',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 2'),
        ),
        migrations.AlterField(
            model_name='student_name_m_4',
            name='score_3',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 3'),
        ),
        migrations.AlterField(
            model_name='student_name_m_4',
            name='score_4',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 4'),
        ),
        migrations.AlterField(
            model_name='student_name_m_4',
            name='score_5',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 5'),
        ),
        migrations.AlterField(
            model_name='student_name_m_4',
            name='score_6',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 6'),
        ),
        migrations.AlterField(
            model_name='student_name_m_4',
            name='score_7',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 7'),
        ),
        migrations.AlterField(
            model_name='student_name_m_4',
            name='score_8',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 8'),
        ),
        migrations.AlterField(
            model_name='student_name_m_4',
            name='score_9',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนที่ 9'),
        ),
        migrations.AlterField(
            model_name='technology_chapter_content_m5',
            name='chapter_id',
            field=models.CharField(max_length=2000, verbose_name='บทที่'),
        ),
        migrations.AlterField(
            model_name='technology_chapter_content_m5',
            name='chapter_name',
            field=models.CharField(max_length=2000, verbose_name='ชื่อบท'),
        ),
        migrations.AlterField(
            model_name='technology_chapter_content_m5',
            name='content',
            field=models.CharField(max_length=2000, verbose_name='ลิงก์เนื้อหา iframe'),
        ),
        migrations.AlterField(
            model_name='technology_chapter_content_m5',
            name='content_video',
            field=models.CharField(default='0', max_length=2000, verbose_name='ลิงก์เนื้อหา วิดีโอ'),
        ),
        migrations.AlterField(
            model_name='technology_chapter_content_m5',
            name='lasttime',
            field=models.CharField(max_length=2000, verbose_name='ระยะเวลา'),
        ),
        migrations.AlterField(
            model_name='technology_chapter_content_m5',
            name='textwork',
            field=models.CharField(max_length=2000, verbose_name='อธิบายใบงาน'),
        ),
        migrations.AlterField(
            model_name='technology_chapter_content_m5',
            name='work',
            field=models.CharField(max_length=2000, verbose_name='ลิงก์ใบงาน รูปภาพ'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='first_name',
            field=models.CharField(max_length=2000, verbose_name='ชื่อจริง'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='last_name',
            field=models.CharField(max_length=2000, verbose_name='นามสกุล'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_1',
            field=models.CharField(default='1', max_length=2000, verbose_name='ใบงานที่ 1'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_2',
            field=models.CharField(default='2', max_length=2000, verbose_name='ใบงานที่ 2'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_3',
            field=models.CharField(default='3', max_length=2000, verbose_name='ใบงานที่ 3'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_4',
            field=models.CharField(default='4', max_length=2000, verbose_name='ใบงานที่ 4'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_5',
            field=models.CharField(default='5', max_length=2000, verbose_name='ใบงานที่ 5'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_6',
            field=models.CharField(default='6', max_length=2000, verbose_name='ใบงานที่ 6'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_7',
            field=models.CharField(default='7', max_length=2000, verbose_name='ใบงานที่ 7'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_8',
            field=models.CharField(default='8', max_length=2000, verbose_name='ใบงานที่ 8'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='name_work_9',
            field=models.CharField(default='9', max_length=2000, verbose_name='ใบงานที่ 9'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_1',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 1'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_2',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 2'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_3',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 3'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_4',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 4'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_5',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 5'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_6',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 6'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_7',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 7'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_8',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 8'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='score_9',
            field=models.IntegerField(default='0', max_length=2000, verbose_name='คะแนนใบงานที่ 9'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='work_success_student_1',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 1'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='work_success_student_2',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 2'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='work_success_student_3',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 3'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='work_success_student_4',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 4'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='work_success_student_5',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 5'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='work_success_student_6',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 6'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='work_success_student_7',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 7'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='work_success_student_8',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 8'),
        ),
        migrations.AlterField(
            model_name='technology_student_name_m_5',
            name='work_success_student_9',
            field=models.CharField(default='0', max_length=2000, verbose_name='ผลงานที่เสร็จ 9'),
        ),
    ]
