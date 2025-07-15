### 1. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate 

### 2. Install dependencies
pip install -r requirements.txt
playwright install


### 3. Set up Redis (run in separate terminal)
redis-server  

### 4. Apply migrations
python manage.py makemigrations
python manage.py migrate


### 5. Start the Celery worker (in separate terminal)
celery -A urlshot_project worker --loglevel=info --pool=solo


### 6. Start the Django development server
python manage.py runserver


### ✅ 1. Submit a Screenshot Request (via Postman or curl)
POST `http://127.0.0.1:8000/screenshots`
{
  "url": "https://www.capgemini.com/",
  "webhook_url": "https://webhook.site/5ae0c116-e65c-41b9-80ed-bb1d332dd718"
}

> Replace webhook_url with one from https://webhook.site

### ✅ 2. Check Webhook Callback
Go to your webhook.site tab — you should receive:
{
  "job_id": "1ee344ed-ebbd-4c1b-897a-a458f46a9e83",
  "status": "completed",
  "screenshot_url": "/media/1ee344ed-ebbd-4c1b-897a-a458f46a9e83.png"
}

### ✅ 3. View Screenshot
Open this URL in your browser:
http://127.0.0.1:8000/media/1ee344ed-ebbd-4c1b-897a-a458f46a9e83.png
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/61f62cfe-ba98-4d99-b07b-0bd3e3b8c2bd" />


### ✅ 4. Check Status
GET `http://127.0.0.1:8000/media/screenshots/1ee344ed-ebbd-4c1b-897a-a458f46a9e83/status`

### ✅ 5. Get Screenshot Metadata
GET `http://127.0.0.1:8000/media/screenshots/1ee344ed-ebbd-4c1b-897a-a458f46a9e83`
