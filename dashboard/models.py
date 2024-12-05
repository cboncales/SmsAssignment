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
            account_sid = 'AC21b99e8bcef5e45fe1f0731ac932eb30'
            auth_token = '8bf3f2d2c10d433dba45f85aee7dcf3d'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Congratulations! {self.name}, your score is {self.score}",
                from_="+15418033420",
                to="09486994790",
            )
        else:
            account_sid = 'AC21b99e8bcef5e45fe1f0731ac932eb30'
            auth_token = '8bf3f2d2c10d433dba45f85aee7dcf3d'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Sorry {self.name}, your score is {self.score}. Try again",
                from_="+15418033420",
                to="09486994790",
            )

            print(message.sid)
            return super().save(*args, **kwargs)