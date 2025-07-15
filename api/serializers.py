from rest_framework import serializers
from .models import ScreenshotJob

class ScreenshotRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenshotJob
        fields = ['url', 'webhook_url']

class ScreenshotStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenshotJob
        fields = ['job_id', 'status']

class ScreenshotMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenshotJob
        fields = ['job_id', 'url', 'created_at']