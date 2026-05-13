=======
# AIoT Child Monitoring (Local)

This project uses OpenCV DNN (Caffe MobileNet-SSD) to detect people from a camera stream and trigger alerts through a FastAPI endpoint. Alerts can be sent via Telegram and/or Gmail based on .env toggles.

## Project Layout
```
child_monitoring_AIOT/
├─ ai.py
├─ alert_system.py
├─ server.py
├─ telegram_alert.py
├─ example.env
├─ requirements.txt
└─ README.md
```

## Setup
1. Create a virtual environment.
2. Install dependencies:
>>>>>>> f6db460 (Updated README & minor changes)
```
pip install -r requirements.txt
```
3. Copy example.env to .env and update the values.

## Configuration (.env)
Copy example.env to .env and fill in the values below:
- USE_ESPCAM / USE_LAPTOP_CAM: set one to true, the other to false.
- ESP32_STREAM_URL: required when USE_ESPCAM=true.
- NO_PERSON_ALERT_TIME: seconds to wait before triggering an alert.
- ENABLE_EMAIL_ALERT / ENABLE_TELEGRAM_ALERT: toggle alert channels.
- EMAIL_SENDER / EMAIL_PASSWORD / EMAIL_RECEIVER: Gmail SMTP settings.
- TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID: Telegram alert settings.
- PROTOTXT_PATH / WEIGHTS_PATH: paths to the Caffe model files.

For Gmail, use a Google App Password (recommended).

## Run
Start the API server (FastAPI):
```
python -m uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

Start the AI detection loop:
```
python ai.py
```

Optional: run the Telegram bot for manual commands:
```
python telegram_alert.py
```

Optional: send a one-off alert test:
```
python alert_system.py
```
This will send notifications based on the configured settings.

## TO RUN THE PROGRAM

- Fill the required things in .env file;
- make the changes needed there.

### Server
`uvicorn server:app --reload to`

### Telegram bot
`py telegram_alert.py`

### main file
`py ai.py`
```
