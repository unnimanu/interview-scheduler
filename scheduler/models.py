from django.db import models
from django.contrib.auth.models import User


class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)
    interview_date = models.DateField(max_length=255, null=True, blank=True)

    def __str__(self):
        return u"%s" % self.user
