import cv2
import numpy as np
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

USE_ESPCAM = os.getenv("USE_ESPCAM", "false").lower() == "true"
USE_LAPTOP_CAM = os.getenv("USE_LAPTOP_CAM", "false").lower() == "true"
ESP32_STREAM_URL = os.getenv("ESP32_STREAM_URL", "")
NO_PERSON_ALERT_TIME = int(os.getenv("NO_PERSON_ALERT_TIME", 10))

prototxt_path = os.getenv("PROTOTXT_PATH")
weights_path = os.getenv("WEIGHTS_PATH")


net = cv2.dnn.readNetFromCaffe(prototxt_path, weights_path)


if USE_ESPCAM:
    cap = cv2.VideoCapture(ESP32_STREAM_URL)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    print("[INFO] Using ESP32-CAM stream")
elif USE_LAPTOP_CAM:
    cap = cv2.VideoCapture(0)
    print("[INFO] Using Laptop Camera")
else:
    raise Exception("❌ No valid camera source configured in .env")

alert_sent = False
no_person_start_time = None
print("[INFO] Starting video stream...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("[WARN] Failed to grab frame. Retrying...")
        time.sleep(1)
        continue

    h, w = frame.shape[:2]


    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    person_count = 0
    max_confidence = 0

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        class_id = int(detections[0, 0, i, 1])

        if confidence > 0.6 and class_id == 15:
            person_count += 1
            max_confidence = max(max_confidence, confidence)

            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x1, y1, x2, y2) = box.astype("int")

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"Person {confidence*100:.2f}%", 
                        (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)


    cv2.putText(frame, f"People: {person_count}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, f"Max Confidence: {max_confidence*100:.2f}%", (10, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)


    if person_count == 0:
        if no_person_start_time is None:
            no_person_start_time = time.time()
        elif time.time() - no_person_start_time >= NO_PERSON_ALERT_TIME and not alert_sent:
            print(f"⚠️ ALERT! No person detected for {NO_PERSON_ALERT_TIME} seconds.")
            try:
                response = requests.post("http://127.0.0.1:8000/trigger_alert")
                print("✅ Alert Sent:", response.json())
            except requests.exceptions.RequestException as e:
                print("❌ Alert Error:", e)
            alert_sent = True
    else:
        no_person_start_time = None
        alert_sent = False

    cv2.imshow("AI Person Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
