from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ScreenshotJob
from .serializers import *
import uuid
from .tasks import process_screenshot
from django.http import FileResponse, Http404
import os

class ScreenshotCreate(APIView):
    def post(self, request):
        data = request.data.copy()
        job_id = str(uuid.uuid4())
        data['job_id'] = job_id
        serializer = ScreenshotRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save(job_id=job_id)
            process_screenshot.delay(job_id)
            return Response({'job_id': job_id, 'status': 'queued'})
        return Response(serializer.errors, status=400)

class ScreenshotStatus(APIView):
    def get(self, request, job_id):
        try:
            job = ScreenshotJob.objects.get(job_id=job_id)
            return Response({'job_id': job_id, 'status': job.status})
        except ScreenshotJob.DoesNotExist:
            return Response({'error': 'Not found'}, status=404)

class ScreenshotMetadata(APIView):
    def get(self, request, job_id):
        try:
            job = ScreenshotJob.objects.get(job_id=job_id)
            serializer = ScreenshotMetadataSerializer(job)
            return Response(serializer.data)
        except ScreenshotJob.DoesNotExist:
            return Response({'error': 'Not found'}, status=404)

class ServeScreenshot(APIView):
    def get(self, request, job_id):
        path = f'screenshots/{job_id}.png'
        if os.path.exists(path):
            return FileResponse(open(path, 'rb'), content_type='image/png')
        raise Http404()