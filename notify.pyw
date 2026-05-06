# main.py

from winotify import Notification, audio
import random
from datetime import datetime
import os

# -------- QUOTES -------- #

morning_quotes = [
    "Clock is ticking. Your rank slips with every second wasted.",
    "Wake up or watch your future get crushed by others.",
    "Morning hours decide who eats dust in the final list.",
    "Discipline now or beg for mercy during results.",
    "Laziness today buys regret tomorrow at full price.",
    "Get up. The competition already started while you slept.",
    "Every missed sunrise is a seat given to someone else.",
    "Your dream dies quietly if you hit snooze again.",
    "Start brutal or finish average. Choose before breakfast.",
    "Weak mornings create strong failures in exam hall.",
    "Pressure is here. Face it or get buried by it.",
    "Rise like your rank depends on this single hour.",
    "No warm-up. Attack the day or lose the war.",
    "Comfort kills more JEE dreams than tough questions.",
    "Grind before coffee or cry after results.",
    "The topper is already solving while you stretch.",
    "Morning discipline separates future engineers from future stories.",
    "Delay once, regret forever. Move.",
    "Your future self is watching this exact moment.",
    "Sleep is luxury. Victory is necessity. Pick one.",
    "Morning pain today beats lifetime of “what if.”",
    "Get ruthless with time before time gets ruthless.",
    "First hour sets the tone for your rank. Make it hurt.",
    "Excuses die at sunrise. Results don’t.",
    "The seat is limited. Your time isn’t.",
    "Wake up and earn what others only wish for.",
    "Soft mornings create hard failures.",
    "Start now or explain failure to your parents later.",
    "Every minute idle is a question unsolved forever.",
    "Dawn is unforgiving. Use it or lose everything.",
    "No mercy for slow starters in this race.",
    "Build your rank before the world wakes up."
]

afternoon_quotes = [
    "Slowing down now hands victory to hungrier competitors.",
    "Afternoon dip is where ranks are lost forever.",
    "Push harder or watch your graph flatten and die.",
    "Distraction costs seats. Stay locked in.",
    "The weak rest. The prepared keep bleeding effort.",
    "Momentum dies fast. Kill it or it kills you.",
    "One lazy hour erases three strong mornings.",
    "Comfort is the silent assassin of JEE dreams.",
    "Keep the fire alive or accept mediocrity.",
    "Others are revising while you scroll. Remember that.",
    "Afternoon discipline writes your All India Rank.",
    "Break now and break later during results.",
    "Time pressure doesn’t pause for your mood.",
    "Consistency beats talent when talent takes breaks.",
    "Slow afternoons create fast regrets in June.",
    "Stay brutal. The exam won’t forgive weakness.",
    "Every unchecked notification is a lost mark.",
    "Push through the wall or live behind it forever.",
    "Your competitors don’t get tired. Match them.",
    "Afternoon laziness is future poverty in disguise.",
    "No plateaus allowed. Keep climbing or fall.",
    "Discipline feels heavy now. Regret feels heavier.",
    "Grind without applause. Results will clap later.",
    "The race doesn’t stop when you feel like stopping.",
    "Weak afternoons birth average engineers.",
    "Stay uncomfortable. Comfort has no seat in top ranks.",
    "One slip now multiplies into rank disaster.",
    "Keep moving. Future you demands it.",
    "Distractions are traps. Don’t step in.",
    "Afternoon warriors own the final list.",
    "Energy drops. Discipline doesn’t. Choose.",
    "Maintain the war or lose the war."
]

night_quotes = [
    "What did you actually finish today? Be honest.",
    "Tomorrow’s rank depends on tonight’s review.",
    "Sleep without progress is practice for failure.",
    "Face your undone tasks before closing your eyes.",
    "Night excuses don’t change morning results.",
    "You wasted hours. Own it and fix it now.",
    "Review brutally or repeat the same mistakes.",
    "The day is gone. Did you move closer to your rank?",
    "Weak nights create weak futures. Reflect hard.",
    "Tomorrow starts with tonight’s discipline.",
    "Lies you tell yourself die at midnight.",
    "Unfinished syllabus laughs at your sleep.",
    "Accountability now saves humiliation later.",
    "Count the hours you truly worked. Shocking?",
    "Night is judgment time. Judge yourself harshly.",
    "Rest is earned, not given after half effort.",
    "Your rank is the sum of these nights.",
    "Sleep on excuses. Wake up to regret.",
    "Face the mirror. Are you proud of today?",
    "Every undone question is a future failure.",
    "Night reflection separates survivors from dropouts.",
    "Be strict with yourself or life will be stricter.",
    "Tomorrow’s battle is won in tonight’s silence.",
    "No progress today means no mercy tomorrow.",
    "Write what you lost today. Feel it.",
    "Discipline at night builds legends by morning.",
    "The clock never lies. Neither should you.",
    "End the day stronger than you started.",
    "Night is when real preparation happens.",
    "Waste tonight, explain yourself forever.",
    "Your future is built on these quiet hours.",
    "Sleep only after paying the price in work."
]

hardcore_quotes = [
    "Most of you will fail. Don’t be most.",
    "Talent without discipline is a ticket to nowhere.",
    "Your parents’ sacrifices deserve better than this effort.",
    "Average effort gets average colleges. Accept it.",
    "The world doesn’t owe you a good rank.",
    "Comfort is expensive. Pay now or pay later.",
    "Failure is permanent if you choose ease daily.",
    "Top 100 don’t have your excuses.",
    "This exam will expose every weakness you ignore.",
    "Dreams die when discipline disappears.",
    "You’re running out of attempts. Act like it.",
    "Regret tastes worse than hard work ever will.",
    "No one remembers the almost-toppers.",
    "Your competition is training while you hesitate.",
    "Future poverty starts with today’s procrastination.",
    "The seat is one. The aspirants are lakhs.",
    "Half-prepared students become full-time failures.",
    "Discipline or delusion. Pick one path.",
    "This pain is temporary. The shame isn’t.",
    "You will hate yourself in results if you slack now.",
    "Reality doesn’t care about your potential.",
    "Only consistent animals survive this jungle.",
    "Wasted time compounds into wasted life.",
    "The mirror shows your real enemy every day.",
    "No second chances after the final bell.",
    "Effort now or explanation later. Choose.",
    "Weakness feels good until results day.",
    "Top ranks are built on brutal daily choices.",
    "Your story ends average unless you change tonight.",
    "This is war. Fight dirty with discipline.",
    "Losers hesitate. Winners take everything.",
    "Become unstoppable or remain forgettable."
]

# -------- LOGIC -------- #

def get_quote():
    hour = datetime.now().hour

    if 5 <= hour < 12:
        return random.choice(morning_quotes)
    elif 12 <= hour < 18:
        return random.choice(afternoon_quotes)
    else:
        return random.choice(night_quotes)


def get_hardcore_line():
    return random.choice(hardcore_quotes)


# -------- NOTIFICATION -------- #

def show_notification():
    quote = get_quote()
    hardcore = get_hardcore_line()

    icon_path = os.path.join(os.getcwd(), "icon.ico")

    toast = Notification(
        app_id="Daily Trigger",
        title="🔥 Time to Lock In",
        msg=f"{quote}\n\n{hardcore}",
        duration="long",
        icon=icon_path
    )

    # sound
    toast.set_audio(audio.LoopingAlarm4, loop=False)

    # button (you can change this)
    # toast.add_actions(
    #     label="Start Studying",
    #     launch="https://www.youtube.com"  # replace with your notes / site
    # )

    # toast.add_actions(
    #     label="Ignore 😈",
    #     launch="https://www.google.com"
    # )

    toast.show()


# -------- RUN -------- #

if __name__ == "__main__":
    show_notification()