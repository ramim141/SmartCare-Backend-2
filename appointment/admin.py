from django.contrib import admin
from appointment.models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'doctor_name', 'appointment_type', 'appointment_status', 'time', 'cancel']

    def patient_name(self, obj):
        return obj.patient.user.first_name if obj.patient.user else "No User"

    def doctor_name(self, obj):
        return obj.doctor.user.first_name if obj.doctor.user else "No User"

admin.site.register(Appointment, AppointmentAdmin)
