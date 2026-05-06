from plyer import notification
import random

quotes = [
    "No one is coming to save you.",
    "This is your competition working right now.",
    "Short term pain = long term power.",
]

notification.notify(
    title="Daily Trigger",
    message=random.choice(quotes),
    timeout=10
)