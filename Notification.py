# daily_trigger.py

from plyer import notification
import random
from datetime import datetime

quotes = [
    "You can either scroll or solve.",
    "AIR < 500 is built in silence.",
    "No discipline = no rank.",
    "Someone else is studying right now.",
    "1 hour today = regret avoided tomorrow.",
    "Comfort is your biggest enemy.",
]

def get_time_based_quote():
    hour = datetime.now().hour
    
    if 5 <= hour < 12:
        return "Morning decides your rank."
    elif 12 <= hour < 18:
        return "Don’t waste your prime hours."
    else:
        return "Late night or lazy night? Choose."

def show_notification():
    quote = random.choice(quotes)
    timed_quote = get_time_based_quote()

    message = f"{timed_quote}\n\n{quote}"

    notification.notify(
        title="🔥 Daily Trigger",
        message=message,
        timeout=10,
        app_icon="icon.ico"
    )

if __name__ == "__main__":
    show_notification()