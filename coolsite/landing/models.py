from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50)
    email_client = models.EmailField(blank=True)
    phone = models.CharField(max_length=11)
    # date_meeting = models.DateField(blank=True)
    # place_meeting = models.CharField(max_length=100, blank=True)
    # topic_meeting = models.CharField(max_length=100)
    comment_client = models.TextField(blank=True)

    def __str__(self):
        return f'Имя - {self.name}, Телефон - {self.phone}'
