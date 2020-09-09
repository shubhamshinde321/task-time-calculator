from django.db import models
from users.models import CustomUser


class UserForm(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    project = models.CharField(max_length=255)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    total_time = models.CharField(max_length=255)
    form_submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.task_name)
