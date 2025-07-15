from django.db import models

# Create your models here.

class ScreenshotJob(models.Model):
    job_id = models.CharField(max_length=100, primary_key=True)
    url = models.URLField()
    webhook_url = models.URLField()
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)