# Project STARK (PROTOTYPE)

This project is a real-time AI voice assistant built using LiveKit Agents and Google Gemini Live. The assistant connects to a LiveKit room, listens for user input, generates intelligent responses using Google’s Gemini Realtime models, and speaks those responses back to users using native audio or text-to-speech. The system is designed for low-latency, conversational interactions and is suitable for use in virtual assistants, voice-controlled applications, smart environments, and experimental AI systems.

By leveraging Gemini’s real-time bi-directional generation and LiveKit’s audio streaming infrastructure, the project enables natural, continuous voice conversations with noise cancellation and real-time response handling.

# Requirements & Setup:

To build and run this project, you need the following:

Python 3.10+

LiveKit Agents SDK (Python)

Google Gemini API access (Realtime / Live API enabled)

LiveKit server or LiveKit Cloud account

Environment variables configured via .env

Internet connection for real-time API calls

Required Python Packages

livekit-agents

python-dotenv

openai

LiveKit plugins:
livekit-plugins-google
livekit-plugins-noise-cancellation

# How It Works (High Level)

1. The assistant joins a LiveKit room.

2. User audio input is captured and processed in real time.

3. Google Gemini Live generates responses using bi-directional streaming.

4. Responses are delivered as speech or converted to audio.

5. Audio is streamed back to users through LiveKit with noise cancellation.
