from django.db import models
from django.contrib.auth.models import User

# 1. ข้อมูลพนักงาน
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # เชื่อมกับระบบ Login
    nickname = models.CharField(max_length=50, verbose_name="ชื่อเล่น")
    role = models.CharField(max_length=20, choices=[('Doctor', 'หมอ'), ('Nurse', 'พยาบาล'), ('Staff', 'พนักงาน')])
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="เงินเดือนพื้นฐาน")
    
    def __str__(self):
        return self.user.first_name

# 2. ระบบการลา
class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50, choices=[('Sick', 'ลาป่วย'), ('Annual', 'ลาพักร้อน')])
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, default='Pending') # Pending, Approved, Rejected