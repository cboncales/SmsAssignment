from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Appointment

def cancel_appointment_view(request, appointment_id):
    # Get the appointment
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    # Cancel it
    appointment.cancel_appointment()

    # Return a response
    return JsonResponse({'message': 'Appointment canceled successfully!'})
