from django.db import models
from django.conf import settings
from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse


class Appointment(models.Model):
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    appointment_date = models.DateTimeField()
    is_notified = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)  # New field for cancellation

    def __str__(self):
        return f"{self.customer_name} - {self.appointment_date}"

    def save(self, *args, **kwargs):
        VONAGE_BRAND_NAME = "Vonage APIs"
        TO_NUMBER = self.phone_number

        if not self.is_notified and not self.is_canceled:
            # Send reminder SMS
            text_message = (
                f"Hello {self.customer_name}, this is a reminder for your appointment on "
                f"{self.appointment_date.strftime('%Y-%m-%d %H:%M:%S')}. Please contact us if you have questions."
            )
            self._send_sms(TO_NUMBER, VONAGE_BRAND_NAME, text_message)
            self.is_notified = True

        # Save the model instance
        super().save(*args, **kwargs)

    def cancel_appointment(self):
        """
        Mark the appointment as canceled and send a cancellation SMS.
        """
        if not self.is_canceled:
            self.is_canceled = True  # Mark as canceled

            VONAGE_BRAND_NAME = "Vonage APIs"
            TO_NUMBER = self.phone_number

            # Send cancellation SMS
            cancel_message = (
                f"Hello {self.customer_name}, your appointment scheduled on "
                f"{self.appointment_date.strftime('%Y-%m-%d %H:%M:%S')} has been canceled. Please contact us for rescheduling."
            )
            self._send_sms(TO_NUMBER, VONAGE_BRAND_NAME, cancel_message)

            # Save the updated status
            self.save()

    def _send_sms(self, to_number, from_name, message_text):
        """
        Utility method to send SMS using Vonage.
        """
        client = Vonage(
            Auth(api_key=settings.VONAGE_API_KEY, api_secret=settings.VONAGE_API_SECRET)
        )
        try:
            message = SmsMessage(
                to=to_number,
                from_=from_name,
                text=message_text,
            )
            response: SmsResponse = client.sms.send(message)

            if response.messages[0].status == "0":
                print("SMS sent successfully.")
            else:
                print(f"Failed to send SMS: {response.messages[0].error_text}")
        except Exception as e:
            print(f"Error sending SMS: {e}")
