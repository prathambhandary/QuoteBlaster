# main.py

from winotify import Notification, audio
import random
from datetime import datetime
import os

# -------- QUOTES -------- #

morning_quotes = [
    "Clock is ticking. Get up or stay average.",
    "Weak mornings birth weak ranks.",
    "Rise now. Comfort dies in the exam hall.",
    "Your competitors woke up an hour ago.",
    "Delay today, regret tomorrow’s rank.",
    "Morning discipline separates future IITians.",
    "No snooze button in competition.",
    "Get up. The paper won’t solve itself.",
    "Every lazy morning costs you a seat.",
    "Start brutal or finish ordinary.",
    "Sun is up. Your excuses aren’t.",
    "First hour decides the day’s rank.",
    "Sleep is temporary. Regret is permanent.",
    "Morning pain beats exam hall shame.",
    "Wake up like your future depends on it.",
    "Champions don’t negotiate with alarms.",
    "You’re already behind. Move.",
    "Early grind writes your success story.",
    "Skip this morning, repeat last year’s rank.",
    "Discipline before sunrise builds legends.",
    "Time lost at dawn kills dreams at dusk.",
    "Get in the chair. Now.",
    "Your rank is being decided right now.",
    "Lazy start, painful cutoff.",
    "Morning weakness invites future failure.",
    "Rise. The competition never sleeps.",
    "One weak morning can destroy months.",
    "Start ugly. Finish first.",
    "Comfort in bed costs seats in IIT.",
    "Dawn discipline or lifetime regret.",
    "Your future self is watching this morning.",
    "Get up. Average students are still sleeping.",
    "Morning hours are non-negotiable.",
    "Hesitate now, cry during results.",
    "Build momentum before the world wakes.",
    "First step out of bed decides everything.",
    "No warm-up. Attack the day.",
    "Sleep less, rank higher.",
    "Morning excuses become June regrets.",
    "The paper is coming. Prepare like it.",
    "Weak mornings make strong competitors win.",
    "Start now or watch others celebrate.",
    "Alarm ignored is opportunity wasted.",
    "Grind before breakfast or beg later.",
    "Your rank doesn’t wait for motivation.",
    "Morning discipline is the only shortcut.",
    "Get ruthless with the clock.",
    "Today’s sunrise won’t repeat.",
    "Rise brutally or remain average forever.",
    "Every second in bed is a lost mark.",
    "Morning warriors clear cutoffs. Others don’t.",
    "Start strong. Mediocrity waits for no one.",
    "The seat is reserved for the disciplined.",
    "Wake up. Your dream is under attack.",
    "No mercy for slow starters."
]

afternoon_quotes = [
    "Afternoon slip costs evening regret.",
    "Distraction now, rejection letter later.",
    "Keep pushing. Fatigue is temporary.",
    "Slowing down is how you lose seats.",
    "One lazy hour kills daily targets.",
    "Phone in hand, rank in gutter.",
    "Maintain war pace. Exam is near.",
    "Afternoon weakness invites night guilt.",
    "Push harder when energy drops.",
    "Consistency dies in comfortable afternoons.",
    "You’re not tired. You’re undisciplined.",
    "Break now, break later in results.",
    "Momentum lost is hard to recover.",
    "Average students rest. You don’t.",
    "Afternoon distractions create future failures.",
    "Grind through the dip or regret it.",
    "Focus slips today, cutoff misses tomorrow.",
    "Stay uncomfortable. Comfort loses ranks.",
    "No social media. No mercy.",
    "Keep moving or fall behind permanently.",
    "Tired is not an excuse.",
    "Afternoon warriors secure top ranks.",
    "One break becomes many.",
    "Discipline doesn’t take naps.",
    "Your competitors are still solving problems.",
    "Slow afternoon equals stressful night.",
    "Push. The clock doesn’t care.",
    "Distraction is the enemy inside.",
    "Maintain intensity. Cutoffs don’t lower.",
    "Energy low? Discipline takes over.",
    "Afternoon comfort is future poison.",
    "Stay locked in or stay ordinary.",
    "Every wasted minute hurts your rank.",
    "No recovery for lost hours.",
    "Grind now. Celebrate after results.",
    "Fatigue talks. Don’t listen.",
    "Afternoon focus separates dreamers from doers.",
    "Keep the pressure on yourself.",
    "Slowing is quitting in disguise.",
    "One weak afternoon ruins weeks.",
    "Stay brutal. The exam won’t forgive.",
    "Distractions today, tears in June.",
    "Momentum is everything. Protect it.",
    "Average pace gets average ranks.",
    "Push past the wall. It’s there.",
    "No excuses in the middle of war.",
    "Afternoon discipline builds night peace.",
    "Stay hungry. Results are coming.",
    "Comfort kills more dreams than failure.",
    "Keep attacking problems. No breaks.",
    "Your rank is bleeding right now.",
    "Hold the line. Don’t slip.",
    "Tired minds don’t crack JEE.",
    "Afternoon grind pays night sleep.",
    "Stay dangerous with your time."
]

night_quotes = [
    "What did you actually finish today?",
    "Review your excuses. They cost seats.",
    "Night guilt beats morning regret.",
    "Tomorrow repeats today’s effort.",
    "Be honest. Did you waste hours?",
    "Sleep only after targets are met.",
    "Unfinished tasks become lifelong regrets.",
    "Night reflection exposes daily lies.",
    "You know exactly where you slacked.",
    "Tomorrow’s rank depends on tonight’s honesty.",
    "Weak day? Fix it before sleep.",
    "No targets hit, no peace.",
    "Account for every wasted minute.",
    "Night is judgment time.",
    "Sleep on excuses, wake up behind.",
    "Review brutally. Improve ruthlessly.",
    "Today’s gaps become tomorrow’s failures.",
    "Did you earn today’s sleep?",
    "Honest night audit builds champions.",
    "Unchecked days create failed students.",
    "Plan tomorrow like today failed.",
    "Night comfort without work is theft.",
    "Face your shortcomings before closing eyes.",
    "Tomorrow starts with tonight’s decisions.",
    "Average effort, average future.",
    "Sleep is earned, not given.",
    "Track every hour. No hiding.",
    "Night questions reveal true commitment.",
    "Fix today or repeat next year.",
    "Guilt now prevents bigger pain later.",
    "Be strict with your night review.",
    "Unproductive day equals painful results.",
    "Tomorrow’s warrior reviews tonight.",
    "No lies at the end of day.",
    "Sleep heavy only after grinding.",
    "Night accountability shapes morning action.",
    "Count marks lost to laziness.",
    "Honest reflection or continued delusion.",
    "Prepare tomorrow’s battle plan now.",
    "Weak nights create weak ranks.",
    "Face reality before lights out.",
    "Today’s effort determines your seat.",
    "No excuses when reviewing alone.",
    "Night discipline fuels morning fire.",
    "Tomorrow you will thank tonight’s pain.",
    "Measure progress. Adjust ruthlessly.",
    "Sleep with targets or wake with regret.",
    "Daily failure compounds fast.",
    "Night is where real students improve.",
    "Be accountable or stay average.",
    "Review cuts deeper than any teacher.",
    "Fix gaps before they widen.",
    "Tomorrow repeats unless you change.",
    "End strong. Start stronger.",
    "Night truth sets morning free."
]

hardcore_quotes = [
    "Most of you will fail. Don’t be most.",
    "Talent loses to discipline every time.",
    "Your excuses won’t appear on the rank list.",
    "Comfort now, regret for decades.",
    "Thousands are better prepared than you.",
    "Half-hearted effort guarantees half seat.",
    "JEE doesn’t care about your feelings.",
    "Future you hates current lazy you.",
    "Average students don’t get IIT.",
    "Pain of discipline or pain of regret.",
    "Cutoffs don’t adjust for your mood.",
    "You’re competing against the ruthless.",
    "Wasted time is permanent loss.",
    "Dreams die in distraction.",
    "Rank decides life. Act like it.",
    "No one remembers second place here.",
    "Your competitors are suffering right now.",
    "Easy path leads to ordinary life.",
    "Failure here follows you forever.",
    "Discipline or cope later.",
    "Seats are limited. Effort isn’t.",
    "Stop lying to yourself.",
    "The exam is unforgiving. Match it.",
    "Comfort is the silent killer.",
    "Most quit. That’s why ranks exist.",
    "Your future is being decided daily.",
    "Regret is expensive. Pay now.",
    "No participation trophies in JEE.",
    "Weakness today, rejection tomorrow.",
    "Reality doesn’t negotiate.",
    "Only consistent survive cutoffs.",
    "Dream big, work brutal.",
    "Time is cruel to the lazy.",
    "You chose this war. Fight.",
    "Failure is permanent if you quit.",
    "IIT isn’t for the soft.",
    "Daily compromise creates lifetime compromise.",
    "The mirror shows your real enemy.",
    "Ranks don’t lie. Effort does.",
    "Suffer now or suffer later.",
    "Everyone wants the seat. Few earn it.",
    "Your pace is your destiny.",
    "Distraction is self-betrayal.",
    "The paper will expose every weakness.",
    "No second chances after results.",
    "Grind like your life depends on it.",
    "Average is the enemy.",
    "Consequences are coming. Prepare.",
    "Laziness today, lower branch forever.",
    "Only the obsessed clear this.",
    "Time pressure doesn’t wait.",
    "Regret tastes worse than hard work.",
    "Seats go to the relentless.",
    "Face the brutal truth daily.",
    "Become unstoppable or stay unseen.",
    "You’re not tired. You’re avoiding hard work.",
    "No one cares how hard you tried without results.",
    "Results expose effort. Nothing else.",
    "You don’t deserve a rank you didn’t earn.",
    "Average effort is invisible in results.",
    "Your competition doesn’t feel sorry for you.",
    "Every excuse is self-sabotage.",
    "You’re either improving or falling behind.",
    "There is no ‘maintaining’ your level.",
    "Comfort today deletes opportunity tomorrow.",
    "Your rank is a direct reflection of discipline.",
    "Nobody remembers almost clearing the cutoff.",
    "You chose distraction. Now choose the consequence.",
    "Effort isn’t equal. Results prove it.",
    "If it was easy, everyone would make it.",
    "You’re competing with obsession, not motivation.",
    "Your future won’t match your intentions.",
    "You can’t cheat consistency.",
    "This exam rewards only the relentless.",
    "You’re not unlucky. You’re underprepared.",
    "Every shortcut cuts your own future.",
    "Hard truth: you’re not doing enough yet.",
    "Discipline is the only unfair advantage.",
    "Your habits are writing your result already.",
    "You don’t fail suddenly. You fail daily.",
    "Missed hours don’t come back during revision.",
    "You’re building your result right now.",
    "No one is behind you. They’re ahead.",
    "Effort without intensity is wasted time.",
    "The exam exposes every weak habit.",
    "Your comfort zone has no rank holders.",
    "You’re either feared or forgotten.",
    "No grind, no glory. Simple math.",
    "Delusion feels good. Results don’t.",
    "You know what you’re avoiding.",
    "Stop negotiating with laziness.",
    "Every distraction is a decision.",
    "You’re training your brain to quit.",
    "Consistency is rare. That’s why ranks are too.",
    "If you slow down, others pass you.",
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