from django.shortcuts import render
from .models import Employee, Attendance
from .utils import load_excel_data


def attendance_report(request):
    load_excel_data()
    dates = Attendance.objects.values_list('date',flat=True).distinct().order_by('date')
    employees = Employee.objects.all()
    report = []
    for employee in employees:
        row = {
            'employee': employee,
            'attendance': []
        }
        for date in dates:
            try:
                att = Attendance.objects.get(employee=employee, date=date)
                row['attendance'].append({
                    'date' : date,
                    'working_hours' : att.working_hours,
                    'start_time' : att.start_time,
                    'end_time' : att.end_time,
                })
            except:
                row['attendance'].append({
                    'date' : date,
                    'working_hours' : 'N/A',
                    'start_time' : 'N/A',
                    'end_time' : 'N/A',
                })
        report.append(row)
    return render(request,'attendance_report.html', {'report': report, 'dates': dates})
