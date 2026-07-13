TASK 1 · Voice Assistant
Objective: Build a Python-based voice assistant that listens to spoken commands and responds with useful actions. Beginners implement core voice recognition; advanced builds add NLP, API integrations, and smart home features.
Tech Stack: Python, speech_recognition library, pyttsx3 (text-to-speech), datetime, webbrowser — Advanced additionally uses: nltk or transformers, third-party APIs (weather, email), smtplib
Feature Checklist — Beginner Tier:
[ ] Capture voice input using speech_recognition (microphone)
[ ] Respond to "Hello" with a predefined greeting
[ ] Tell the current time and date on request
[ ] Perform a web search on a user-specified topic (open browser with query)
[ ] Graceful error handling: if voice is not understood, ask the user to repeat
[ ] Text-to-speech feedback using pyttsx3 for all responses
Made using Ollama mistral model 0.30.0, an interactive local llm based assistant that can do and answer any simple task. 