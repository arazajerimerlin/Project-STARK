# Project STARK

this project is a real-time AI voice assistant built using LiveKit Agents and OpenAI. It connects to a LiveKit room, listens for user input, generates intelligent responses using OpenAI’s GPT-4o Realtime model, and converts those responses into spoken audio using text-to-speech. The assistant is designed for low-latency, interactive voice conversations and can be used in applications such as virtual assistants, voice-controlled systems, smart rooms, or experimental AI agents.

The system separates language understanding (LLM) from speech output (TTS), ensuring stability and flexibility. OpenAI handles natural language generation, while LiveKit manages real-time audio streaming, noise cancellation, and room communication.

# Requirements & Setup:

To build and run this project, you need the following:

Python 3.10+

LiveKit Agents SDK (Python)

OpenAI API key (with access to gpt-4o-realtime-preview)

LiveKit server or LiveKit Cloud account

Environment variables configured via .env

Internet connection for real-time API calls

Required Python Packages

livekit-agents

python-dotenv

openai

LiveKit plugins:
livekit-plugins-openai
livekit-plugins-noise-cancellation

# How It Works (High Level):

The assistant joins a LiveKit room.

User input is captured and processed in real time.

OpenAI generates a text response using GPT-4o Realtime.

The response text is converted into speech.

The spoken reply is streamed back into the LiveKit room.
