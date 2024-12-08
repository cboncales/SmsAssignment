from django.db import models
from django.conf import settings
from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse

class Appointment(models.Model):
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    appointment_date = models.DateTimeField()
    is_notified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer_name} - {self.appointment_date}"

    def save(self, *args, **kwargs):
        # Vonage configurations
        VONAGE_BRAND_NAME = "Vonage APIs"
        TO_NUMBER = self.phone_number

        # Format the SMS message
        text_message = (
            f"Hello {self.customer_name}, this is a reminder for your appointment on "
            f"{self.appointment_date.strftime('%Y-%m-%d %H:%M:%S')}. Please contact us if you have questions."
        )

        # Initialize Vonage client
        client = Vonage(
            Auth(api_key=settings.VONAGE_API_KEY, api_secret=settings.VONAGE_API_SECRET)
        )
        
        # Send SMS if not already notified
        if not self.is_notified:
            try:
                message = SmsMessage(
                    to=TO_NUMBER,
                    from_=VONAGE_BRAND_NAME,
                    text=text_message,
                )
                response: SmsResponse = client.sms.send(message)

                if response.messages[0].status == "0":
                    print("SMS sent successfully.")
                    self.is_notified = True  # Mark as notified
                else:
                    print(
                        f"Failed to send SMS: {response.messages[0].error_text}"
                    )
            except Exception as e:
                print(f"Error sending SMS: {e}")

        # Save the model instance
        super().save(*args, **kwargs)
