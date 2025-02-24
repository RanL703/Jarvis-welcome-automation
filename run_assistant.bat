@echo off
setlocal

REM Try to use Python from Windows default location
set PYTHON_CMD="%LOCALAPPDATA%\Programs\Python\Python311\python.exe"

REM If not found, try Microsoft Store Python
if not exist %PYTHON_CMD% (
    set PYTHON_CMD="%LOCALAPPDATA%\Microsoft\WindowsApps\python3.exe"
)

REM Check if Python exists
%PYTHON_CMD% --version >nul 2>&1
if errorlevel 1 (
    echo Python not found! Please install Python from python.org
    echo Visit: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Create and activate venv
cd /d "%~dp0"
if not exist venv (
    echo Creating virtual environment...
    %PYTHON_CMD% -m venv venv
)

REM Activate venv and install dependencies
call venv\Scripts\activate.bat
if not exist venv\Scripts\pip.exe (
    echo Installing pip...
    python -m ensurepip --upgrade
)

echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo Starting assistant...
python voice_assistant.py
pause
