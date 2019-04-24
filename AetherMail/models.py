from django.db import models
from django.conf import settings
from django.utils import timezone
#from django.contrib.auth.models import AbstractUser

# Create your models here.
'''
class user(models.Model):
    name = models.TextField(max_length=40, null=False, blank=False)
    username = '''


READ_STATUS_CHOICES = [("r","R"),("u","U")]
TRASH_STATUS_CHOICES = [("y","Y"),("n","N")]

class Message(models.Model):
    from_user = models.CharField(max_length=20, blank=True, null=True)
    to_user = models.CharField(max_length=20, blank=False, null=False)
    subject = models.CharField(max_length=100)
    body = models.TextField(null=False, blank=False)
    timestamp = models.DateTimeField(blank=True, null=True)
    read_status = models.CharField(max_length=1, blank=False, null=False, choices= READ_STATUS_CHOICES, default="U")
    received_trash_status = models.CharField(max_length=1, blank=False, null=False, choices=TRASH_STATUS_CHOICES, default='N')
    sent_trash_status = models.CharField(max_length=1, blank=False, null=False, choices=TRASH_STATUS_CHOICES, default='N')


    def set_timestamp(self):
        self.timestamp = timezone.now()
        self.save()

    def get_subject(self):
        return self.subject

    def __str__(self):
        return self.subject

    #def delete_msg(self):
    #    self.delete()



'''
class CustomUser(AbstractUser):

    def __str__(self):
        return self.email
'''