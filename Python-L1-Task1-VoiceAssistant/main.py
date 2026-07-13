import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import whisper
import requests
from gtts import gTTS
import pygame
import os
import time
import string


whisper_model = whisper.load_model("base", device="cpu")


conversation_history = ""


def speak(text):
    print("DIP:", text)

    filename = "voice.mp3"

    for i in range(3):  
        try:
            tts = gTTS(text=text, lang='hi')
            tts.save(filename)

            pygame.mixer.init()
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                continue

            pygame.mixer.quit()

            if os.path.exists(filename):
                os.remove(filename)

            return

        except Exception as e:
            print(f"TTS Error (attempt {i+1}):", e)
            time.sleep(1)

    print("TTS failed completely")
def listen():
    print("Listening... You can speak now")

    fs = 16000
    duration = 4

    try:
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()

        write("input.wav", fs, recording)

        
        # print("File exists:", os.path.exists("input.wav"))
        # print("File size:", os.path.getsize("input.wav"))

        
        if os.path.getsize("input.wav") < 1000:
            print("Audio too small, ignored")
            return ""

        
        result = whisper_model.transcribe("input.wav", language="hi", fp16=False)

        text = result["text"].strip().lower()

        # print("You said:", text)

        return text

    except Exception as e:
        print("Listen error:", e)
        return ""


def ask_ai(prompt):
    global conversation_history

    conversation_history += "User: " + prompt + "\n"

    try:
        #print("Inside ask_ai()")

        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": "Reply in simple words.\n" + conversation_history,
                "stream": False
            },
            timeout=30
        )

        #print("HTTP Status:", response.status_code)

        data = response.json()

        #print("JSON received")

        ai_reply = data.get("response", "")

        #print("AI Reply:", repr(ai_reply))

        conversation_history += "DIP: " + ai_reply + "\n"

        return ai_reply

    except Exception as e:
     print("AI ERROR:", repr(e))
     return "Sorry, something went wrong."
speak("नमस्ते! मैं डी का असिस्टेंट हूँ। आज मैं आपकी कैसे मदद कर सकता हूँ?")
while True:
    command = listen()

    if not command or len(command.strip()) < 2:
        print("Ignored empty input")
        continue

    print("RAW:", repr(command))

    clean = command.lower().strip()
    clean = clean.translate(str.maketrans('', '', string.punctuation))

    if any(word in clean for word in ["exit", "bye", "goodbye", "stop"]):
        speak("Goodbye! Have a nice day.")
        break

    #print("Calling ask_ai()...")

    response = ask_ai(command)

    #print("Returned from ask_ai()")
    #print("Response:", repr(response))

    print("Calling speak()...")

    speak(response)

    print("Finished speaking")