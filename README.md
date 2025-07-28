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

Rename `example.env` to `.env` and add your credentials:
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
