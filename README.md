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
**POST** `http://127.0.0.1:8000/screenshots`
{
  "url": "https://example.com",
  "webhook_url": "https://webhook.site/your-custom-id"
}


> Replace webhook_url with one from https://webhook.site

### ✅ 2. Check Webhook Callback
Go to your webhook.site tab — you should receive:
{
  "job_id": "...",
  "status": "completed",
  "screenshot_url": "/media/<job_id>.png"
}

### ✅ 3. View Screenshot
Open this URL in your browser:
http://127.0.0.1:8000/media/<job_id>.png

### ✅ 4. Check Status
GET `http://127.0.0.1:8000/screenshots/<job_id>/status`

### ✅ 5. Get Screenshot Metadata
GET `http://127.0.0.1:8000/screenshots/<job_id>`
