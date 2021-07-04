from django.shortcuts import render
from.models import *


def index(request):  # ตั้งชื่อฟังก์ชั่นให้ตรงกับ path ใน urls.py
    # สร้างตัวแปร blog เพื่อเก็บข้อมูลได้ที่จากฐานข้อมูลทั้งหมด
    subject = Subject_head.objects.all()

    data_sub = {"subject": subject}

    # ส่งข้อมูลในรูปแบบ object )
    return render(request, 'index.html', {'data': data_sub})
    # เมื่อมีการทำงานของฟังก์ชั่น index จะถูก render ไปยัง index.html


def class_room(request, id=None):
    subject = Subject_head.objects.filter(id=id)
    data_sub = {"subject": subject}

    # ออกแบบ ม.4
    name_m4 = Student_name_m_4.objects.all()
    data_name_m4 = {"name_m4": name_m4}

    content_m4 = Chapter_content_m4.objects.all()
    data_content_m4 = {"content_m4": content_m4}

    # ออกแบบ ม.5
    Design_content_m5 = Design_Chapter_content_m5.objects.all()
    data_Design_content_m5 = {"Design_content_m5": Design_content_m5}

    Design_name_m5 = Design_Student_name_m_5.objects.all()
    data_Design_name_m5 = {"Design_name_m5": Design_name_m5}

    # เทคโนโลยี ม.5
    Technology_content_m5 = Technology_Chapter_content_m5.objects.all()
    data_Technology_content_m5 = {
        "Technology_content_m5": Technology_content_m5}

    Technology_name_m5 = Technology_Student_name_m_5.objects.all()
    data_Technology_name_m5 = {"Technology_name_m5": Technology_name_m5}

    # SBMLD ม.6
    name_m6 = SBMLD_Student_name_m_6.objects.all()
    data_name_m6 = {"name_m6": name_m6}

    content_m6 = SBMLD_Chapter_content_m6.objects.all()
    data_content_m6 = {"content_m6": content_m6}

    context = {'data': data_sub, 'm4': data_name_m4,
               'content_D4': data_content_m4, 'content_D5': data_Design_content_m5, 'mD5': data_Design_name_m5, 'content_T5': data_Technology_content_m5, 'mT5': data_Technology_name_m5, 'm6': data_name_m6,
               'content_SBMLD6': data_content_m6, }
    return render(request, 'class_room.html', context)
