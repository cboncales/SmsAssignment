from django.db import models
from twilio.rest import Client

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.score >= 70:
            account_sid = 'AC7d9f2bb7122d257079b9ff8f63424d57'
            auth_token = '58ca37aa07c77e804a6ee4ba00e8cef2'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Congratulations! {self.name}, your score is {self.score}",
                from_="+14173863503",
                to="+639486994790",
            )

            print(message.body)
        else:
            account_sid = 'AC7d9f2bb7122d257079b9ff8f63424d57'
            auth_token = '58ca37aa07c77e804a6ee4ba00e8cef2'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Sorry {self.name}, your score is {self.score}. Try again",
                from_="+14173863503",
                to="+639486994790",
            )

            print(message.body)
            return super().save(*args, **kwargs)