from django.urls import path
from .views import *

urlpatterns = [
    path('screenshots', ScreenshotCreate.as_view()),
    path('screenshots/<str:job_id>/status', ScreenshotStatus.as_view()),
    path('screenshots/<str:job_id>', ScreenshotMetadata.as_view()),
    path('screenshots/<str:job_id>.png', ServeScreenshot.as_view()),
]