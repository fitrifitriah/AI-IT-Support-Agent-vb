#!/bin/bash
# Production startup script for AI IT Support Agent
# This script ensures the app starts correctly with proper checks

set -e  # Exit on error

echo "🚀 Starting AI IT Support Agent..."
echo "=================================="

# Check if API key is set
if [ -z "$GEMINI_API_KEY" ]; then
    echo "❌ ERROR: GEMINI_API_KEY environment variable is not set!"
    echo "Please set it in Dewacloud environment variables."
    exit 1
fi

echo "✓ API Key found"

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Install/update dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip setuptools
pip install -r requirements.txt

echo "✓ Dependencies installed"

# Run health check
echo "🔍 Verifying API connectivity..."
python3 -c "
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

# Start Streamlit app
echo ""
echo "=================================="
echo "🎯 Starting Streamlit Application"
echo "=================================="
echo ""
echo "✓ Access the app at: http://localhost:8501"
echo "✓ Remote access: https://your-dewacloud-app-url"
echo ""

# Start the app
streamlit run app.py \
    --server.port=8501 \
    --server.address=0.0.0.0 \
    --logger.level=info \
    --client.toolbar.mode=minimal
