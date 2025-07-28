from fastapi import FastAPI
from alert_system import send_alert
from datetime import datetime

app = FastAPI()

@app.post("/trigger_alert")  # Ensure this is POST
def trigger_alert():
    try:
        alert_id = send_alert()
        return {
            "status": "success",
            "message": "Alert Sent",
            "alert_id": alert_id,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "status": "error",
            "message": "Failed to send alert",
            "error": str(e)
        }

@app.get("/get_alert")  # Simple GET endpoint for testing
def get_alert():
    return {"status": "Alert system is running"}
