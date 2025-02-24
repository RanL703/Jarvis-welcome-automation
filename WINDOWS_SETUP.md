# Windows Setup Guide

1. Prerequisites:
   - Install [Python](https://www.python.org/downloads/) (3.8 or higher)
   - Install [Ollama](https://ollama.ai/download)
   - Install [PowerToys](https://github.com/microsoft/PowerToys/releases/)

2. Copy Project:
   - Open `\\wsl$\Ubuntu\home\flickshot\THISisSOfkingCOOL` in Explorer
   - Copy to `C:\Users\YourUsername\Projects\THISisSOfkingCOOL`

3. Environment Setup:
   - Copy `.env.example` to `.env`
   - Get Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Update `.env` with your API key

4. First Run:
   - Double-click `run_assistant.bat`
   - It will automatically:
     - Create virtual environment
     - Install dependencies
     - Launch the assistant

5. Test Setup:
   - Say "Wake up daddy's home"
   - Should activate your CODE workspace
   - Should hear a welcome message

6. Troubleshooting:
   - Run `python test_without_voice.py` to test without voice
   - Check microphone in Windows Sound settings
   - Verify PowerToys workspace named "CODE" exists
