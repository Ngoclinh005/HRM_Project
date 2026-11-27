from django.db import models


class Employee(models.Model):

    # Trạng thái làm việc
    STATUS_CHOICES = [
        ('active', 'Đang làm việc'),
        ('probation', 'Thử việc'),
        ('leave', 'Nghỉ phép'),
        ('resigned', 'Đã nghỉ việc'),
    ]

    GENDER_CHOICES = [
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác'),
    ]

    # Thông tin nhân viên
    employee_code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Mã nhân viên'
    )

    full_name = models.CharField(
        max_length=100,
        verbose_name='Họ và tên'
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True,
        verbose_name='Giới tính'
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name='Ngày sinh'
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        verbose_name='Số điện thoại'
    )

    email = models.EmailField(
        blank=True,
        verbose_name='Email'
    )

    address = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Địa chỉ'
    )

    department = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Phòng ban'
    )

    position = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Chức vụ'
    )

    start_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Ngày vào làm'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name='Trạng thái'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Ngày tạo'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Ngày cập nhật'
    )

    def __str__(self):
        return f'{self.employee_code} - {self.full_name}'

    class Meta:
        verbose_name = 'Nhân viên'
        verbose_name_plural = 'Danh sách nhân viên'
        ordering = ['employee_code']