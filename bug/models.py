from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class CustUser(AbstractUser):
    display_name = models.CharField(max_length=30, null=True, blank=True)   


class BugModel(models.Model):
    NEW = 'NO'
    IN_PROGRESS = 'IP'
    DONE = 'DO'
    INVALID = 'IN'
    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid'),
    ]

    title = models.CharField(max_length=40)
    time_created = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    author = models.ForeignKey(
        CustUser, related_name='%(class)s_author', null=True,
        blank=True, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        CustUser, related_name='%(class)s_owner', null=True,
        blank=True, on_delete=models.CASCADE)
    closer = models.ForeignKey(
        CustUser, related_name='%(class)s_closer', null=True,
        blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NEW)


    def __str__(self):
        return self.title
