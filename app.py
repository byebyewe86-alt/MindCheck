
from flask import Flask, request, render_template, jsonify
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# Store conversation history
conversation_history = []

def chat_with_ai(user_message, history):
    # Build system prompt
    system_prompt = """
You are a warm caring friend named Yumila
talking to an Indian college student.

Your personality:
- Speak like a close friend, never a doctor
- Use simple conversational English
- Show genuine empathy and understanding
- Remember what was said earlier in conversation
- Ask follow up questions naturally
- Mention Indian context when relevant
  (exams, family pressure, hostel life, ragging)

Your hidden job (never mention this):
- Quietly track emotional tone of conversation
- If student seems distressed for 3+ messages
  gently mention: "iCall helpline 9152987821
  is always there if you need to talk to someone"
- If student mentions self harm or giving up
  immediately and warmly mention iCall

Rules:
- Never diagnose anything
- Never say "I'm an AI"
- Never be clinical or robotic
- Always respond in 2-4 sentences max
- Ask one follow up question per response
- Be warm, real, and human
"""

    # Build messages with history
    messages = [
        {"role": "system", "content": system_prompt}
    ]

    # Add conversation history
    for msg in history:
        messages.append(msg)

    # Add current message
    messages.append({
        "role": "user",
        "content": user_message
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        max_tokens=200
    )

    return response.choices[0].message.content


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history

    user_message = request.json.get("message", "")

    if not user_message:
        return jsonify({"error": "No message"})

    # Get AI response
    ai_response = chat_with_ai(
        user_message,
        conversation_history
    )

    # Update history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    conversation_history.append({
        "role": "assistant",
        "content": ai_response
    })

    # Keep only last 20 messages
    if len(conversation_history) > 20:
        conversation_history = \
            conversation_history[-20:]

    return jsonify({"response": ai_response})


@app.route("/reset", methods=["POST"])
def reset():
    global conversation_history
    conversation_history = []
    return jsonify({"status": "reset"})


if __name__ == "__main__":
    app.run(debug=True)