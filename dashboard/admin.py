from django.contrib import admin
from .models import Appointment

@admin.action(description='Cancel selected appointments')
def cancel_appointments(modeladmin, request, queryset):
    for appointment in queryset:
        appointment.cancel_appointment()

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'phone_number', 'appointment_date', 'is_notified', 'is_canceled']
    list_filter = ['is_notified', 'is_canceled']  
    search_fields = ['customer_name', 'phone_number']
    actions = [cancel_appointments]

admin.site.register(Appointment, AppointmentAdmin)
