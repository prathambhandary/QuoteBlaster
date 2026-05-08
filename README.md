# QuoteBlaster

A Python-based notification system designed to reinforce discipline through timed, high-impact reminders.

This project is built for students preparing for competitive exams such as JEE. It focuses on consistency, accountability, and maintaining focus throughout the day.

---

## Features

* Time-based notifications (morning, afternoon, night)
* Categorized quote system (discipline, consistency, reflection, and pressure)
* Windows notifications with sound support
* Action buttons for quick access to study resources
* Lightweight and suitable for background execution

---

## Project Structure

```
daily_trigger/
│── icon.ico              # Notification icon
│── Notification.py       # Core notification logic
│── notify.py             # Main script
│── notify.pyw            # Background execution (no terminal)
│── main.lnk              # Shortcut for quick launch
│── requirements.txt      # Dependencies
│── README.md
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/daily-trigger.git
cd daily-trigger
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## Usage

Run the script:

```
python notify.py
```

For background execution without a terminal window:

```
python notify.pyw
```

---

## Automation

To run the script automatically, use Windows Task Scheduler:

1. Open Task Scheduler
2. Create a Basic Task
3. Set Trigger to Daily (recommended times: morning, afternoon, night)
4. Set Action to Start a Program

   * Program: `pythonw`
   * Argument: `path\to\notify.pyw`

This ensures notifications are delivered consistently without manual execution.

---

## Example Output

<img width="2132" height="1212" alt="589622445-2bce61b3-f40c-43da-862f-189143ec13d8" src="https://github.com/user-attachments/assets/8fc51aef-80f7-450f-bb92-51fbb0c13ccf" />


---

## Quote System

Quotes are divided into the following categories:

* Morning: Focus on urgency and starting the day effectively
* Afternoon: Maintain consistency and avoid productivity drops
* Night: Encourage reflection and accountability
* Hardcore: Direct and strict reminders to maintain discipline

All quotes can be modified or extended in the main script.

---

## Customization

### Modify notification actions

```
toast.add_actions(
    label="Start Studying",
    launch="file:///C:/path/to/your/notes.pdf"
)
```

### Change notification sound

```
from winotify import audio
toast.set_audio(audio.LoopingAlarm, loop=False)
```

### Add or edit quotes

Update the quote lists in `notify.py`.

---

## Future Improvements

* Study streak tracking
* Distraction management integration
* Mobile notification support
* Adaptive notification behavior based on user activity

---

## License

This project is licensed under the MIT License.

---

## Purpose

The goal of this project is to create a consistent external trigger that supports disciplined study habits and reduces reliance on motivation alone.
