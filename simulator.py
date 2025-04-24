import requests
import random
import time

url = "http://127.0.0.1:5000/data"

while True:
    data = {
        "temperature": round(random.uniform(25, 35), 2),
        "humidity": round(random.uniform(60, 90), 2)
    }
    try:
        requests.post(url, json=data)
        print("Sent:", data)
    except Exception as e:
        print("Failed to send:", e)
    time.sleep(2)  # Send every 2 seconds
