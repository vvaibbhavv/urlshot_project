from celery import shared_task
from .models import ScreenshotJob
from playwright.sync_api import sync_playwright
import requests, os

@shared_task
def process_screenshot(job_id):
    print(f"[Celery Task] Processing job_id: {job_id}")
    
    try:
        job = ScreenshotJob.objects.get(job_id=job_id)
    except ScreenshotJob.DoesNotExist:
        print(f"[ERROR] ScreenshotJob with job_id {job_id} does not exist.")
        return

    path = f'screenshots/{job_id}.png'
    os.makedirs('screenshots', exist_ok=True)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(job.url)
            page.screenshot(path=path)
            browser.close()

        job.status = 'completed'
        job.save()

        payload = {
            'job_id': job_id,
            'status': 'completed',
            'screenshot_url': f'/media/{job_id}.png'
        }
        requests.post(job.webhook_url, json=payload)
        print(f"[SUCCESS] Webhook sent for job_id: {job_id}")

    except Exception as e:
        job.status = 'failed'
        job.save()
        print(f"[ERROR] Exception while processing job {job_id}: {e}")
