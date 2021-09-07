from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Add Function show Table name


class Subject_headAdminSite(admin.ModelAdmin):
    model = Subject_head
    list_display = ("title_sub", "code_sub", "teacher")


class Student_name_m_4AdminSite(admin.ModelAdmin):
    model = Student_name_m_4
    list_display = ("first_name", "last_name", "score_1", "score_2",
                    "score_3", "score_4", "score_5", "score_6", "score_7", "score_8", "score_9", "score_midterm", "score_finalterm", "sum_score")


class Design_Student_name_m_5AdminSite(admin.ModelAdmin):
    model = Design_Student_name_m_5
    list_display = ("first_name", "last_name", "score_1", "score_2",
                    "score_3", "score_4", "score_5", "score_6", "score_7", "score_8", "score_9", "score_midterm", "score_finalterm", "sum_score")


class Technology_Student_name_m_5AdminSite(admin.ModelAdmin):
    model = Technology_Student_name_m_5
    list_display = ("first_name", "last_name", "name_work_1", "score_1", "name_work_2", "score_2", "name_work_3",
                    "score_3", "name_work_4", "score_4", "name_work_5", "score_5", "name_work_6", "score_6", "name_work_7", "score_7", "name_work_8", "score_8", "name_work_9", "score_9", "sum_score")


class SBMLD_Student_name_m_6AdminSite(admin.ModelAdmin):
    model = Technology_Student_name_m_5
    list_display = ("first_name", "last_name", "name_work_1", "score_1", "name_work_2", "score_2", "name_work_3",
                    "score_3", "name_work_4", "score_4", "name_work_5", "score_5", "name_work_6", "score_6", "name_work_7", "score_7", "name_work_8", "score_8", "name_work_9", "score_9", "sum_score")


class Chapter_content_m4AdminSite(admin.ModelAdmin):
    model = Subject_head
    list_display = ("chapter_id", "chapter_name", "check_recently")


class Design_Chapter_content_m5AdminSite(admin.ModelAdmin):
    model = Subject_head
    list_display = ("chapter_id", "chapter_name", "check_recently")


class Technology_Chapter_content_m5AdminSite(admin.ModelAdmin):
    model = Subject_head
    list_display = ("chapter_id", "chapter_name", "check_recently")


class SBMLD_Chapter_content_m6AdminSite(admin.ModelAdmin):
    model = Subject_head
    list_display = ("chapter_id", "chapter_name", "check_recently")


# Register your models here.
admin.site.register(Subject_head, Subject_headAdminSite)
admin.site.register(Student_name_m_4, Student_name_m_4AdminSite)
admin.site.register(Design_Student_name_m_5, Design_Student_name_m_5AdminSite)
admin.site.register(Technology_Student_name_m_5,
                    Technology_Student_name_m_5AdminSite)
admin.site.register(SBMLD_Student_name_m_6,
                    SBMLD_Student_name_m_6AdminSite)
admin.site.register(Chapter_content_m4, Chapter_content_m4AdminSite)
admin.site.register(Design_Chapter_content_m5,
                    Design_Chapter_content_m5AdminSite)
admin.site.register(Technology_Chapter_content_m5,
                    Technology_Chapter_content_m5AdminSite)
admin.site.register(SBMLD_Chapter_content_m6,
                    SBMLD_Chapter_content_m6AdminSite)


admin.site.site_header = format_html(
    '<div style="color:#ffffff">ระบบสอนส่วนหลังบ้านโดย วัชกร บุตร์ดีวงษ์</div>')
admin.site.site_title = 'หน้าหลัก'
admin.site.index_title = 'ระบบสอนออนไลน์'
