from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'phone_number', 'appointment_date', 'is_notified']
    list_filter = ['is_notified']
    search_fields = ['customer_name', 'phone_number']

admin.site.register(Appointment, AppointmentAdmin)
