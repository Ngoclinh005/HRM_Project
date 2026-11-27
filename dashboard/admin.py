from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    # Các cột hiển thị trong danh sách
    list_display = (
        'employee_code',
        'full_name',
        'department',
        'position',
        'phone',
        'email',
        'status',
    )

    # Tìm kiếm nhân viên
    search_fields = (
        'employee_code',
        'full_name',
        'phone',
        'email',
    )

    # Bộ lọc bên phải
    list_filter = (
        'department',
        'position',
        'status',
        'gender',
    )

    # Sắp xếp theo mã nhân viên
    ordering = ('employee_code',)

    # Không cho sửa trực tiếp ngày tạo
    readonly_fields = ('created_at', 'updated_at')