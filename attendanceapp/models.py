from django.db import models

class Employee(models.Model):
    employee_id = models.IntegerField(unique = True)
    name = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    working_hours = models.FloatField(default = 0)

    def __str__(self):
        return f"{self.employee.name} - {self.date}"



