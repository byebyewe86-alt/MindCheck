# MindCheck
# 🧠 MindCheck — AI Mental Health Companion

## The Problem
1 in 4 Indian college students struggle with 
stress, anxiety or depression. Most stay silent 
due to stigma, fear of judgment, or simply not 
knowing where to turn.

The hardest part? When you're truly struggling,
you don't want to fill a form or get a risk score.
You just want someone to listen.

## The Solution
MindCheck is a private AI companion that talks 
with Indian college students like a caring friend.
Unlike clinical apps that ask you to fill forms,
MindCheck just listens and remembers what you said.

## What Makes It Different

| Feature | Other Apps | MindCheck |
|---------|-----------|-----------|
| Interaction | One time form | Continuous conversation |
| Memory | Forgets each session | Remembers full context |
| Tone | Clinical assessment | Caring friend |
| Focus | Generic advice | Indian specific context |
| Crisis | Shows number always | Shows naturally when needed |
| Control | App decides | User always in control |

## How It Works
```
Student opens app
      ↓
Types how they feel naturally
      ↓
AI responds like a caring friend
      ↓
Conversation continues with memory
      ↓
If distress detected over multiple messages
AI gently mentions iCall helpline
      ↓
Student feels heard — not assessed
```

## Features
- Real time chat without page reloads
- Full conversation memory across messages
- Typing animation while AI thinks
- Detects hidden distress in casual language
- Indian specific context awareness:
  → Hostel life and loneliness
  → Exam pressure and results
  → Family expectations
  → Ragging and bullying
  → Competitive exam burnout
- New Chat button for fresh start
- Crisis helpline always visible in footer
- Mobile friendly design
- API key secured with environment variables

## Tech Stack
```
Backend:
Python 3.13
Flask — web framework
Groq API — AI inference
Llama 3.3 70B — language model

Frontend:
HTML5 + CSS3
JavaScript fetch API
JSON for data exchange

Security:
python-dotenv for API key protection
```

## Project Structure
```
MindCheck/
├── app.py              ← Flask backend + AI logic
├── templates/
│   └── index.html      ← Chat interface
├── .env                ← API key (not on GitHub)
├── .gitignore          ← Protects .env
└── README.md           ← This file
```

## How The AI Works

**Conversation Memory:**
Full chat history is sent with every API call.
This gives the AI complete context so it can
say "you mentioned hostel life earlier" and
build a genuine supportive conversation.

**Natural Distress Detection:**
Instead of asking "rate your stress 1-10"
the AI detects distress naturally through
conversation — the same way a real friend would
notice something is wrong without asking directly.

**Indian Context Awareness:**
The AI is specifically prompted to understand
Indian college life — hostel loneliness, exam
pressure, family expectations, ragging, and
competitive exam burnout like JEE and NEET.

**User Always In Control:**
The app never alerts anyone, never shares data,
never acts without the student's knowledge.
Crisis resources are shown gently and naturally
— never forced.

## Why We Built This

Built from personal experience of hostel life
and the loneliness of new surroundings in 1st year.

Watching fellow students struggle silently while
pretending everything was fine inspired this project.

MindCheck doesn't replace human connection.
It triggers it.

## Crisis Resources

- 📞 iCall: 9152987821 (free, confidential)
- 📞 Vandrevala Foundation: 1860-2662-345
- 📞 AASRA: 9820466627 (available 24/7)
- 📞 UGC Anti Ragging: 1800-180-5522

## Future Improvements

- Voice input so students can speak freely
- Silence detection across sessions
- Pattern tracking over time
- Optional anonymous counselor connection
- Hindi and regional language support

## Built By
Solo Project | 1st Year B.Tech Student
Mental Health Track | Student Wellness Initiative
