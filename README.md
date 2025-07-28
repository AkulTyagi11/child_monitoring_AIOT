## Folder Structure
```
AIoT-Child-Monitoring/
│── esp32_cam/                  # ESP32-CAM firmware (Microcontroller Code)
│   ├── esp32_cam.ino           # Main ESP32-CAM Arduino code
│   ├── config.h                # Wi-Fi and server configuration
│   ├── camera_config.h         # ESP32-CAM camera settings
│   ├── libraries/              # External libraries for ESP32-CAM
│
│── backend/                     # AI Processing + API (Runs on Laptop)
│   ├── ai_processing.py         # AI-based person detection (YOLO, OpenCV)
│   ├── alert_system.py          # Sends alerts (Twilio, Firebase)
│   ├── server.py                # Flask API to receive ESP32-CAM stream
│   ├── requirements.txt         # Python dependencies
│   ├── models/                  # AI models (YOLO, TensorFlow)
│   │   ├── yolov8n.pt           # Pre-trained YOLO model
│
│── frontend/                    # Web Dashboard (React.js)
│   ├── public/                  # Static assets (icons, images)
│   ├── src/                     # Main React source code
│   │   ├── components/          # React components
│   │   │   ├── VideoFeed.jsx    # Live video component
│   │   │   ├── Alerts.jsx       # Notification display
│   │   ├── pages/               # Web pages
│   │   │   ├── Dashboard.jsx    # Parent dashboard page
│   │   ├── App.js               # Main React app
│   │   ├── index.js             # React entry point
│   ├── package.json             # React dependencies
│
│── mobile_app/                   # Mobile App (Optional)
│   ├── app.js                    # React Native app
│   ├── components/                # Mobile components
│   ├── package.json               # Mobile app dependencies
│
│── docs/                         # Documentation
│   ├── system_architecture.md     # System architecture explanation
│   ├── api_endpoints.md           # API documentation
│
│── .gitignore                     # Ignore unnecessary files
│── README.md                       # Project overview & setup instructions

```

## Explanation of Each Folder
- esp32_cam/ → Stores ESP32-CAM firmware (Arduino code)
- backend/ → Contains AI detection & server API (Flask, OpenCV)
- frontend/ → Web-based dashboard (React.js) for live monitoring
- mobile_app/ → (Optional) Mobile app to view live feed & alerts
- docs/ → Project documentation & API details

## Notification Feature

This project includes a Notification System that can send alerts via Telegram and Gmail. You can configure it to send notifications through one or both services based on your preference.

### Telegram Notification

- Uses a Telegram bot to send alerts to a specified chat.
- Requires a Telegram Bot Token and Chat ID.
- Can be toggled on/off in the settings.

### Gmail Notification

- Sends email alerts using SMTP.
- Requires a Google App Password for authentication.
- Can be toggled on/off in the settings.

### Configuration

Rename `.env.example` to `.env` and add your credentials:
```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=receiver_email@gmail.com
```
Ensure your bot is active and has permission to send messages.
Enable Less Secure Apps or use App Passwords for Gmail.

### Usage

Run the alert system:

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