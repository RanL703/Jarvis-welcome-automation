import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import requests
import subprocess
from dotenv import load_dotenv
import os
import socket

# Load environment variables
load_dotenv()

# Configuration
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
OLLAMA_URL = os.getenv('OLLAMA_URL', 'http://localhost:11434/api/generate')
WAKE_PHRASE = os.getenv('WAKE_PHRASE', "wake up daddy's home")
WORKSPACE_SHORTCUT = os.getenv('WORKSPACE_SHORTCUT', r'C:\Users\RANADEEP LASKAR\Desktop\CODE.lnk')

class VoiceAssistant:
    def __init__(self):
        # Initialize Windows SAPI5 TTS engine
        self.engine = pyttsx3.init(driverName='sapi5')
        self.engine.setProperty('rate', 180)
        
        # Initialize speech recognizer
        self.recognizer = sr.Recognizer()
        
        # Setup Gemini
        genai.configure(api_key=GEMINI_API_KEY)
        self.gemini = genai.GenerativeModel('gemini-pro')

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def is_connected(self):
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except OSError:
            return False

    def get_ai_response(self, prompt):
        if self.is_connected():
            try:
                response = self.gemini.generate_content(prompt)
                return response.text
            except Exception as e:
                print(f"Gemini API error: {str(e)}")
                return self.get_ollama_response(prompt)
        return self.get_ollama_response(prompt)

    def get_ollama_response(self, prompt):
        try:
            response = requests.post(OLLAMA_URL, json={
                'model': 'deepseek-r1:1.5b',
                'prompt': prompt
            })
            return response.json().get('response', "Welcome back, commander!")
        except requests.RequestException as e:
            print(f"Ollama API error: {str(e)}")
            return "Welcome back, commander! Working in offline mode."
        except ValueError as e:
            print(f"JSON parsing error: {str(e)}")
            return "Welcome back, commander! Working in offline mode."

    def detect_wake_phrase(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source, phrase_time_limit=5)
        
        try:
            text = self.recognizer.recognize_google(audio).lower()
            return WAKE_PHRASE in text
        except (sr.UnknownValueError, sr.RequestError) as e:
            print(f"Speech recognition error: {str(e)}")  # Log the error
            return False

    def activate_workspace(self):
        try:
            subprocess.run(['start', WORKSPACE_SHORTCUT], shell=True)
            prompt = "Generate a snarky welcome message about coffee and coding, and add something like 'ready to make something amazing?' to acknowledge that all development programs are now open"
            response = self.get_ai_response(prompt)
            self.speak(response)
        except Exception as e:
            error_msg = f"Error activating workspace: {str(e)}"
            print(error_msg)  # Log the error
            self.speak("Had trouble opening your workspace, but I'm still here for you!")

    def run(self):
        print("Assistant is ready...")
        while True:
            if self.detect_wake_phrase():
                self.activate_workspace()

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()
