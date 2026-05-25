@echo off
REM Production startup script for AI IT Support Agent (Windows)
REM This script ensures the app starts correctly with proper checks

echo.
echo 🚀 Starting AI IT Support Agent...
echo ==================================
echo.

REM Check if API key is set
if "%GEMINI_API_KEY%"=="" (
    echo ❌ ERROR: GEMINI_API_KEY environment variable is not set!
    echo Please set it in your environment or Dewacloud dashboard.
    pause
    exit /b 1
)

echo ✓ API Key found

REM Check Python version
python --version
if errorlevel 1 (
    echo ❌ ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo.
echo 📦 Installing dependencies...
pip install --upgrade pip setuptools
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo ✓ Dependencies installed

REM Verify API connectivity
echo.
echo 🔍 Verifying API connectivity...
python -c "
import google.generativeai as genai
import os
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError('GEMINI_API_KEY not found')
genai.configure(api_key=api_key)
try:
    models = list(genai.list_models())
    print(f'✓ API connected successfully! Found {len(models)} available models')
except Exception as e:
    print(f'⚠ Warning: Could not verify API: {e}')
"

REM Start Streamlit app
echo.
echo ==================================
echo 🎯 Starting Streamlit Application
echo ==================================
echo.
echo ✓ Access the app at: http://localhost:8501
echo ✓ Remote access: https://your-dewacloud-app-url
echo.

streamlit run app.py ^
    --server.port=8501 ^
    --server.address=0.0.0.0 ^
    --logger.level=info ^
    --client.toolbar.mode=minimal

pause
