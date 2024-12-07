from django.db import models
from django.conf import settings 
from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Vonage configurations
        VONAGE_BRAND_NAME = "Vonage APIs"
        TO_NUMBER = "639486994790"

        # Initialize the Vonage client
        client = Vonage(
        Auth(api_key=settings.VONAGE_API_KEY, api_secret=settings.VONAGE_API_SECRET))

        # Prepare the SMS message
        if self.score >= 70:
            text_message = f"Congratulations! {self.name}, your score is {self.score}"
        else:
            text_message = f"Sorry {self.name}, your score is {self.score}. Try again."

        message = SmsMessage(
            to=TO_NUMBER,
            from_=VONAGE_BRAND_NAME,
            text=text_message,
        )

        # Send the SMS and handle the response
        try:
            response: SmsResponse = client.sms.send(message)
            if response.messages[0].status == "0":
                print("Message sent successfully.")
            else:
                print(
                    f"Message failed with error: {response.messages[0].error_text}"
                )
        except Exception as e:
            print(f"Failed to send SMS: {str(e)}")

        # Save the model instance
        return super().save(*args, **kwargs)
