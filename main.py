import feedparser
import requests
import time
from datetime import datetime

RSS_FEEDS = [
    "https://www.reddit.com/r/ClashOfClans/new.rss",
]

WEBHOOK_URL = "https://api.botghost.com/webhook/1518528789779451994/ldmnbk976ll9tf5sbnb4p"

seen_entries = set()

print("CoC RSS Bot Started!")

while True:
    try:
        for feed_url in RSS_FEEDS:
            print(f"[{datetime.now()}] Checking: {feed_url}")
            feed = feedparser.parse(feed_url)
            
            for entry in feed.entries:
                entry_id = entry.get('id', entry.get('link', ''))
                
                if entry_id not in seen_entries:
                    seen_entries.add(entry_id)
                    
                    title = entry.get('title', 'No title')
                    link = entry.get('link', '')
                    
                    payload = {
                        "variables": {
                            "name": title,
                            "message": link
                        }
                    }
                    
                    response = requests.post(WEBHOOK_URL, json=payload)
                    print(f"✓ Sent: {title}")
        
        print(f"Next check in 5 minutes...\n")
        time.sleep(300)
        
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(60)
