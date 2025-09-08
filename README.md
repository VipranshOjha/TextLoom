TextLoom

Weaving AI text into natural human flow, powered by the Gemini API

💬 The Problem

I rely heavily on AI language models for brainstorming, drafting, and summarizing. While they’re great at speed and structure, the outputs often feel robotic — lacking the rhythm, personality, and quirks of natural human writing.

When I searched for online “AI humanizers,” I ran into two big issues:

Expensive Subscriptions → Most good tools are locked behind monthly paywalls.

Severe Character Limits → Free versions barely allowed me to humanize a single paragraph.

That made them impractical for real-world use. I needed something:
✅ Free to run
✅ Capable of handling longer text
✅ Flexible enough to let me choose the tone

✨ The Solution

That’s why I built TextLoom — a local tool that transforms sterile AI text into natural, engaging, human-like writing.

Uses the Google Gemini API through a Flask backend (keeping my API key safe).

Runs as a single-page web app, lightweight and easy to use.

No subscriptions. No limits. Just reliable text humanization whenever I need it.

🚀 Features

🎯 Natural Language Conversion → Smooth, conversational phrasing that feels alive.

🎨 Multiple Tone Selection → Conversational, Professional, Friendly, Witty, Casual, Creative.

🔒 Secure Backend → Flask server ensures your Gemini API key is never exposed.

🖥 Clean & Modern UI → Sleek design for a seamless experience.

📋 One-Click Copy → Copy results instantly.

🔢 Character Counter → Keep track of input length as you write.

⚡ Before/After Comparison → Instantly see how your text improves.

🛠️ Tech Stack

Frontend → HTML, CSS, Vanilla JavaScript

Backend → Python (Flask)

AI Model → Google Gemini API

🖼 Screenshot

(Add a screenshot here — ideally showing both input and output panels side by side)

⚙️ Setup & Usage

Clone the Repository

git clone https://github.com/VipranshOjha/Daily-Problem-Solvers.git
cd Daily-Problem-Solvers/TextLoom


Create the Environment File
Create a .env file in this folder and add your Gemini API key:

GEMINI_API_KEY=YOUR_SECRET_API_KEY_HERE


Install Dependencies

pip install -r requirements.txt


Run the Backend Server

python app.py


Keep this terminal running.

Open the Frontend
Open index.html in your browser.
You’re now ready to use TextLoom 🎉
