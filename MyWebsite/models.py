from django.db import models


"""class TablesNews(models.Model):
    
    # เก็บข้อมูลชนิดรูปภาพแล้วอัพโหลดไปยังโฟลเดอ Photo
    photo = models.ImageField(upload_to="Photo", default='')

    # เก็บข้อมูลประเภท Char มีขนาดมากสุด 1000 ตัวอักษร
    title = models.CharField(max_length=1000)

    # เก็บข้อมูลประเภท Date หรือ วันเวลามีการอัพเดทครั้งเดียวคือตอนบันทึกข้อมูล
    date = models.DateTimeField(auto_now_add=True, blank=False)

    # เก็บข้อมูลประเภท Date หรือวันเวลามีการอัพเดททุกครั้งที่มีการแก้ไขข้อมูล
    date_updated = models.DateTimeField(auto_now_add=True, blank=False)

    # แสดงข้อมูล title ทีหน้า admin
    def __str__(self):
        return self.title"""


class Subject_head(models.Model):
    img = models.ImageField(upload_to="Photo", default='')
    title_sub = models.CharField(max_length=1000)
    name_sub = models.CharField(max_length=5000)
    code_sub = models.CharField(max_length=5000)
    teacher = models.CharField(max_length=5000)

    class Meta:
        verbose_name_plural = "ข้อมูลวิชาทั้งหมด"

    def __str__(self):
        return self.title_sub


# ออกแบบ ม.4


class Student_name_m_4(models.Model):
    first_name = models.CharField(
        max_length=5000, verbose_name="ชื่อจริง")
    last_name = models.CharField(max_length=5000, verbose_name="นามสกุล")
    score_1 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 1")
    score_2 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 2")
    score_3 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 3")
    score_4 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 4")
    score_5 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 5")
    score_6 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 6")
    score_7 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 7")
    score_8 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 8")
    score_9 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 9")

    class Meta:
        verbose_name_plural = "รายชื่อนักเรียนวิชาออกแบบและเทคโนโลยี ม.4"

    def __str__(self):
        return self.first_name

    def sum_score(self):
        sum_scores = [self.score_1, self.score_2, self.score_3, self.score_4,
                      self.score_5, self.score_6, self.score_7, self.score_8, self.score_9]
        sum_scores = [int(x) for x in sum_scores]
        total = 0
        for i in range(0, len(sum_scores)):
            total = total + sum_scores[i]
        return total
    sum_score.short_description = 'คะแนนรวม'

# ออกแบบ ม.5


class Design_Student_name_m_5(models.Model):
    first_name = models.CharField(
        max_length=5000, verbose_name="ชื่อจริง")
    last_name = models.CharField(max_length=5000, verbose_name="นามสกุล")
    score_1 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 1")
    score_2 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 2")
    score_3 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 3")
    score_4 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 4")
    score_5 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 5")
    score_6 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 6")
    score_7 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 7")
    score_8 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 8")
    score_9 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนที่ 9")

    class Meta:
        verbose_name_plural = "รายชื่อนักเรียนวิชาออกแบบและเทคโนโลยี ม.5"

    def __str__(self):
        return self.first_name

    def sum_score(self):
        sum_scores = [self.score_1, self.score_2, self.score_3, self.score_4,
                      self.score_5, self.score_6, self.score_7, self.score_8, self.score_9]
        sum_scores = [int(x) for x in sum_scores]
        total = 0
        for i in range(0, len(sum_scores)):
            total = total + sum_scores[i]
        return total
    sum_score.short_description = 'คะแนนรวม'


# เทคโนโลยี ม.5


class Technology_Student_name_m_5(models.Model):
    first_name = models.CharField(
        max_length=5000, verbose_name="ชื่อจริง")
    last_name = models.CharField(max_length=5000, verbose_name="นามสกุล")
    name_work_1 = models.CharField(
        max_length=5000, default="1", verbose_name="ใบงานที่ 1")
    score_1 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 1")
    work_success_student_1 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 1")
    name_work_2 = models.CharField(
        max_length=5000, default="2", verbose_name="ใบงานที่ 2")
    score_2 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 2")
    work_success_student_2 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 2")
    name_work_3 = models.CharField(
        max_length=5000, default="3", verbose_name="ใบงานที่ 3")
    score_3 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 3")
    work_success_student_3 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 3")
    name_work_4 = models.CharField(
        max_length=5000, default="4", verbose_name="ใบงานที่ 4")
    score_4 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 4")
    work_success_student_4 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 4")
    name_work_5 = models.CharField(
        max_length=5000, default="5", verbose_name="ใบงานที่ 5")
    score_5 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 5")
    work_success_student_5 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 5")
    name_work_6 = models.CharField(
        max_length=5000, default="6", verbose_name="ใบงานที่ 6")
    score_6 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 6")
    work_success_student_6 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 6")
    name_work_7 = models.CharField(
        max_length=5000, default="7", verbose_name="ใบงานที่ 7")
    score_7 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 7")
    work_success_student_7 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 7")
    name_work_8 = models.CharField(
        max_length=5000, default="8", verbose_name="ใบงานที่ 8")
    score_8 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 8")
    work_success_student_8 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 8")
    name_work_9 = models.CharField(
        max_length=5000, default="9", verbose_name="ใบงานที่ 9")
    score_9 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 9")
    work_success_student_9 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 9")

    class Meta:
        verbose_name_plural = "รายชื่อนักเรียนวิชาเทคโนโลยี ม.5"

    def __str__(self):
        return self.first_name

    def sum_score(self):
        sum_scores = [self.score_1, self.score_2, self.score_3, self.score_4,
                      self.score_5, self.score_6, self.score_7, self.score_8, self.score_9]
        sum_scores = [int(x) for x in sum_scores]
        total = 0
        for i in range(0, len(sum_scores)):
            total = total + sum_scores[i]
        return total
    sum_score.short_description = 'คะแนนรวม'

# SBMLD m 6


class SBMLD_Student_name_m_6(models.Model):
    first_name = models.CharField(
        max_length=5000, verbose_name="ชื่อจริง")
    last_name = models.CharField(max_length=5000, verbose_name="นามสกุล")
    name_work_1 = models.CharField(
        max_length=5000, default="1", verbose_name="ใบงานที่ 1")
    score_1 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 1")
    work_success_student_1 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 1")
    name_work_2 = models.CharField(
        max_length=5000, default="2", verbose_name="ใบงานที่ 2")
    score_2 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 2")
    work_success_student_2 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 2")
    name_work_3 = models.CharField(
        max_length=5000, default="3", verbose_name="ใบงานที่ 3")
    score_3 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 3")
    work_success_student_3 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 3")
    name_work_4 = models.CharField(
        max_length=5000, default="4", verbose_name="ใบงานที่ 4")
    score_4 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 4")
    work_success_student_4 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 4")
    name_work_5 = models.CharField(
        max_length=5000, default="5", verbose_name="ใบงานที่ 5")
    score_5 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 5")
    work_success_student_5 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 5")
    name_work_6 = models.CharField(
        max_length=5000, default="6", verbose_name="ใบงานที่ 6")
    score_6 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 6")
    work_success_student_6 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 6")
    name_work_7 = models.CharField(
        max_length=5000, default="7", verbose_name="ใบงานที่ 7")
    score_7 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 7")
    work_success_student_7 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 7")
    name_work_8 = models.CharField(
        max_length=5000, default="8", verbose_name="ใบงานที่ 8")
    score_8 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 8")
    work_success_student_8 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 8")
    name_work_9 = models.CharField(
        max_length=5000, default="9", verbose_name="ใบงานที่ 9")
    score_9 = models.IntegerField(
        max_length=5000, default="0", verbose_name="คะแนนใบงานที่ 9")
    work_success_student_9 = models.CharField(
        max_length=5000, default="0", verbose_name="ผลงานที่เสร็จ 9")

    class Meta:
        verbose_name_plural = "รายชื่อนักเรียนวิชา SBMLD ม.6"

    def __str__(self):
        return self.first_name

    def sum_score(self):
        sum_scores = [self.score_1, self.score_2, self.score_3, self.score_4,
                      self.score_5, self.score_6, self.score_7, self.score_8, self.score_9]
        sum_scores = [int(x) for x in sum_scores]
        total = 0
        for i in range(0, len(sum_scores)):
            total = total + sum_scores[i]
        return total
    sum_score.short_description = 'คะแนนรวม'

# ออกแบบ ม.4


class Chapter_content_m4(models.Model):
    chapter_id = models.CharField(max_length=5000, verbose_name="บทที่")
    chapter_name = models.CharField(
        max_length=5000, verbose_name="ชื่อบท")
    content = models.CharField(
        max_length=5000, verbose_name="ลิงก์เนื้อหา iframe")
    work = models.CharField(max_length=5000,
                            verbose_name="ลิงก์ใบงาน รูปภาพ")
    content_video = models.CharField(
        max_length=5000, verbose_name="ลิงก์เนื้อหา วิดีโอ", default="0")
    lasttime = models.CharField(max_length=5000, verbose_name="ระยะเวลา")

    class Meta:
        verbose_name_plural = "เนื้อหาวิชาออกแบบและเทคโนโลยี ม.4"

    def __str__(self):
        return self.chapter_name

    def check_recently(self):
        if self.lasttime == "ล่าสุด":
            now = True
        else:
            now = False
        return now
    check_recently.boolean = True
    check_recently.short_description = "ใบงานล่าสุด"

# ออกแบบ ม.5


class Design_Chapter_content_m5(models.Model):
    chapter_id = models.CharField(max_length=5000, verbose_name="บทที่")
    chapter_name = models.CharField(
        max_length=5000, verbose_name="ชื่อบท")
    content = models.CharField(
        max_length=5000, verbose_name="ลิงก์เนื้อหา iframe")
    work = models.CharField(max_length=5000,
                            verbose_name="ลิงก์ใบงาน รูปภาพ")
    content_video = models.CharField(
        max_length=5000, verbose_name="ลิงก์เนื้อหา วิดีโอ", default="0")
    lasttime = models.CharField(max_length=5000, verbose_name="ระยะเวลา")

    class Meta:
        verbose_name_plural = "เนื้อหาวิชาออกแบบและเทคโนโลยี ม.5"

    def __str__(self):
        return self.chapter_name

    def check_recently(self):
        if self.lasttime == "ล่าสุด":
            now = True
        else:
            now = False
        return now
    check_recently.boolean = True
    check_recently.short_description = "ใบงานล่าสุด"

# เทคโนโลยี ม.5


class Technology_Chapter_content_m5(models.Model):
    chapter_id = models.CharField(max_length=5000, verbose_name="บทที่")
    chapter_name = models.CharField(
        max_length=5000, verbose_name="ชื่อบท")
    content = models.CharField(
        max_length=5000, verbose_name="ลิงก์เนื้อหา iframe")
    textwork = models.CharField(
        max_length=5000, verbose_name="อธิบายใบงาน")
    work = models.CharField(max_length=5000,
                            verbose_name="ลิงก์ใบงาน รูปภาพ")
    content_video = models.CharField(
        max_length=5000, verbose_name="ลิงก์เนื้อหา วิดีโอ", default="0")
    lasttime = models.CharField(max_length=5000, verbose_name="ระยะเวลา")

    class Meta:
        verbose_name_plural = "เนื้อหาวิชาเทคโนโลยี ม.5"

    def __str__(self):
        return self.chapter_name

    def check_recently(self):
        if self.lasttime == "ล่าสุด":
            now = True
        else:
            now = False
        return now
    check_recently.boolean = True
    check_recently.short_description = "ใบงานล่าสุด"

# เทคโนโลยี ม.5


class SBMLD_Chapter_content_m6(models.Model):
    chapter_id = models.CharField(max_length=5000, verbose_name="บทที่")
    chapter_name = models.CharField(
        max_length=5000, verbose_name="ชื่อบท")
    content = models.CharField(
        max_length=5000, verbose_name="ลิงก์เนื้อหา iframe")
    content_video = models.CharField(
        max_length=5000, verbose_name="ลิงก์เนื้อหา วิดีโอ", default="0")
    chapter_id_work = models.CharField(
        max_length=5000, verbose_name="ใบงานที่")
    example_work = models.CharField(
        max_length=5000, verbose_name="ลิงก์รูปตัวอย่าง")
    textwork = models.CharField(
        max_length=5000, verbose_name="อธิบายใบงาน")
    work = models.CharField(max_length=5000,
                            verbose_name="ลิงก์ใบงาน รูปภาพ")

    lasttime = models.CharField(max_length=5000, verbose_name="ระยะเวลา")

    class Meta:
        verbose_name_plural = "เนื้อหาวิชา SBMLD ม.6"

    def __str__(self):
        return self.chapter_name

    def check_recently(self):
        if self.lasttime == "ล่าสุด":
            now = True
        else:
            now = False
        return now
    check_recently.boolean = True
    check_recently.short_description = "ใบงานล่าสุด"
