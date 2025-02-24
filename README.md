# Voice-Activated Workspace Assistant

A Windows voice assistant that launches your coding workspace with a voice command.

## Features
- Voice activation with customizable wake phrase
- Launches your coding workspace via shortcut
- Snarky AI responses using Gemini (online) or Ollama (offline)
- Text-to-speech feedback

## Windows Setup

1. Install Python 3.11 for Windows from https://python.org

2. Install PyAudio using the provided wheel file:
```powershell
pip install PyAudio-0.2.11-cp311-cp311-win_amd64.whl
```

3. Install other dependencies:
```powershell
pip install -r requirements.txt
```

4. Install Ollama from https://ollama.ai/download (optional - for offline fallback)

5. Pull the Ollama model (if using offline mode):
```powershell
ollama pull deepseek-r1:1.5b
```

6. Configure environment:
   - Copy `.env.example` to `.env`
   - Set your Gemini API key in `.env`
   - Set `WORKSPACE_SHORTCUT` path in `.env` to point to your workspace shortcut

## Setup Your Workspace

### Option 1: PowerToys Workspace (Recommended)
1. Install PowerToys from the [Microsoft Store](https://aka.ms/installpowertoys) or [GitHub](https://github.com/microsoft/PowerToys/releases)
2. Set up a workspace following the [official guide](https://learn.microsoft.com/en-us/windows/powertoys/workspace)
   - Open PowerToys Settings → Workspace
   - Create a new workspace named "CODE"
   - Add your development applications
   - Save the workspace
3. Create a shortcut to activate the workspace:
   - Right-click → New → Shortcut
   - Location: `"C:\Program Files\PowerToys\PowerToys.exe" --workspace "CODE"`
   - Save as `CODE.lnk` on your Desktop

### Option 2: Custom Shortcut
Alternatively, create a standard Windows shortcut that launches your preferred applications.

## Usage

1. Create a shortcut that launches your coding tools
2. Update the `WORKSPACE_SHORTCUT` path in `.env` to point to your shortcut
3. Run the assistant:
```powershell
python voice_assistant.py
```
4. Say "Wake up daddy's home" (or your custom wake phrase)
5. The assistant will:
   - Launch your workspace using the configured shortcut
   - Generate a witty welcome message
   - Switch to Ollama if offline/Gemini fails

## Customization

- Change `WAKE_PHRASE` in `.env` to your preferred activation phrase
- Modify AI model in `get_ollama_response()` if using different Ollama models
- Adjust voice settings in `VoiceAssistant.__init__()`

## Troubleshooting

- If PyAudio installation fails with pip, use the provided wheel file
- Ensure your microphone is working and selected as default input device
- For offline mode, verify Ollama is running (typically at http://localhost:11434)
- For PowerToys workspaces, check the [troubleshooting guide](https://github.com/microsoft/PowerToys/wiki/Workspace-Guide)
