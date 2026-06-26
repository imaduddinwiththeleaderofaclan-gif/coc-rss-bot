import feedparser
import requests
from datetime import datetime

RSS_FEEDS = [
    "https://www.reddit.com/r/ClashOfClans/new.rss",
]

WEBHOOK_URL = "https://api.botghost.com/webhook/1518528789779451994/ldmnbk976ll9tf5sbnb4p"

print("CoC RSS Bot Started!")
print(f"[{datetime.now()}] Checking Reddit...")

feed = feedparser.parse(RSS_FEEDS[0])

for entry in feed.entries[:5]:  # শুধু সর্বশেষ 5টি
    title = entry.get('title', 'No title')
    link = entry.get('link', '')
    
    payload = {
        "variables": {
            "name": title,
            "message": link
        }
    }
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        print(f"✓ Sent: {title[:50]}")
    except Exception as e:
        print(f"Error: {e}")

print("Done!")
