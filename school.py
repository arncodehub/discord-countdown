import os
import requests
from datetime import datetime

def send_webhook(content):
    url = os.getenv("DISCORD_WEBHOOK_URL")
    if not url:
        print("Error: DISCORD_WEBHOOK_URL not found in environment variables.")
        return

    data = {"content": content}
    response = requests.post(url, json=data)
    
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

def calculate_countdown():
    # Set your target date here (Year, Month, Day, Hour, Minute)
    target_date = datetime(2025, 12, 31, 0, 0) 
    now = datetime.now()
    
    diff = target_date - now
    
    if diff.days < 0:
        return "School has ended!"

    if diff.days == 0:
        return "School ends today!"
      
    return f"{diff.days} days until school ends!"

if __name__ == "__main__":
    message = calculate_countdown()
    send_webhook(message)
