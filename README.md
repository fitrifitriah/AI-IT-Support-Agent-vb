# 🤖 AI IT Support Agent - Streamlit Application

A professional Streamlit application powered by Google Gemini AI that analyzes technical support issues and provides structured, actionable responses.

**Live Demo**: https://itsupportagentgemini.user.cloudjkt01.com

## Features

✨ **Smart Issue Analysis**
- Automatic categorization (Hardware, Network, Software, M365)
- Urgency level assessment
- Detailed root cause analysis

📋 **Structured Output**
- Step-by-step troubleshooting guides for IT staff
- Professional email response drafts
- JSON export for integration with other systems

🎨 **User-Friendly Interface**
- Clean, modern design with tabs for different views
- Real-time AI processing with visual feedback
- Download analysis results as JSON
- Copy-to-clipboard functionality for email drafts

---

## 🚀 QUICK START - DEPLOY TO DEWACLOUD (5 Minutes)

### ✅ Step 1: Get Your Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikeys)
2. Click **"Create API Key"**
3. **Copy your key** and save it safely

### ✅ Step 2: Login to Dewacloud

1. Go to [Dewacloud Dashboard](https://dashboard.dewacloud.com)
2. Login with your credentials

### ✅ Step 3: Create New Application

1. Click **"New App"** button
2. Select **"Apache Python 2.4.67"** (or available Python environment)
3. Choose **"Git Repository"** as source

### ✅ Step 4: Configure Repository

In the repository URL field, paste:
```
https://github.com/fitrifitriah/AI-IT-Support-Agent-vb
```

### ✅ Step 5: Configure Start Command

In the **Start Command** / **Run Command** field, paste:

```bash
cd /var/www/webroot/ROOT && pip install -r requirements.txt && python -m streamlit run app.py --server.port=8501 --server.address=0.0.0.0 --server.headless=true
```

### ✅ Step 6: Set Environment Variables

1. Go to **Settings → Environment Variables**
2. Click **"Add Variable"**
3. Add these variables:

| Name | Value |
|------|-------|
| `GEMINI_API_KEY` | `your_api_key_here` (paste your Google key) |

⚠️ **IMPORTANT**: Paste your actual API key from Step 1!

### ✅ Step 7: Deploy

1. Click **"Deploy"** button
2. Wait 3-5 minutes for build to complete
3. Check **Application Servers** tab - status should show ✅ Running
4. Your app is live at: `https://itsupportagentgemini.user.cloudjkt01.com`

### ✅ Step 8: Test the App

1. Click the live URL (you'll see it in the dashboard)
2. Enter a test IT issue, e.g: `"Laptop screen is blank"`
3. Click **"Analyze Issue"**
4. You should see AI analysis with Category, Urgency, Troubleshooting Steps, and Email Draft

**If you see "API key not valid" error**, go back to Step 6 and verify the API key is correct.

---

## 💻 LOCAL DEVELOPMENT SETUP

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Google Gemini API key (from [Google AI Studio](https://aistudio.google.com/app/apikeys))

### Installation

### Installation

**1. Navigate to project:**
```bash
cd "f:\Mini Project\AI IT Support Agent"
```

**2. Create virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # Linux/macOS
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Create .env file:**
```bash
copy .env.example .env
```

**5. Edit .env** - Add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

**6. Run the app:**
```bash
streamlit run app.py
```

Browser will open at: `http://localhost:8501` ✅

---

## 🧪 Testing (Optional)

```bash
# Install test dependencies
pip install -r requirements-dev.txt

# Run all tests
pytest -v

# Run tests with coverage
pytest --cov=. --cov-report=html
```

**Result**: 58 tests passing ✅

1. **Enter Issue Description**: Type a detailed technical issue in the text area
2. **Click "Analyze Issue"**: The AI will process your issue
3. **Review Results**: Check the analysis across different tabs:
   - **Summary**: Quick overview with category and urgency
   - **Root Cause**: Detailed analysis of the problem
   - **Troubleshooting**: Step-by-step guide for IT staff
   - **Email**: Professional response draft for the user
   - **Raw JSON**: Complete structured data
4. **Export**: Download the analysis as JSON or copy the email draft



1. **Enter Issue**: Type a detailed IT issue in the text area
2. **Click "Analyze Issue"**: AI will process and generate analysis
3. **Review Results**: Check different tabs (Summary, Root Cause, Troubleshooting, Email, JSON)
4. **Export**: Download as JSON or copy email draft

### Example Issues

- **Software**: "Excel crashes when opening large spreadsheets"
- **Hardware**: "Monitors flickering throughout the day"
- **Network**: "VPN connection drops randomly"
- **M365**: "Teams has audio delays and latency"

---

## 🎯 Features

✨ **Smart Analysis**
- Automatic issue categorization
- Urgency level assessment
- Root cause identification

📋 **Structured Output**
- Step-by-step troubleshooting
- Professional email drafts
- JSON export for systems integration

🎨 **Professional UI**
- Clean tabbed interface
- Real-time AI processing
- Copy-to-clipboard for emails
- Download results as JSON

---

## ✅ What's Included

## ❓ Troubleshooting

### "API key not valid" Error (Dewacloud)
```
Error: 400 API key not valid
```
**Fix**: Check environment variable in Dewacloud dashboard. Make sure it exactly matches your Google API key.

### "No module named streamlit" (Dewacloud)
**Fix**: The Start Command must include `pip install -r requirements.txt`. Check your configuration and redeploy.

### App returns "Page Temporarily Unavailable" (Dewacloud)
1. Check **Application Servers → Logs**
2. Look for error messages
3. Click **"Redeploy"** to restart
4. Wait 1-2 minutes and refresh browser

### Local: "No module named streamlit"
```bash
pip install -r requirements.txt
```

### Local: Port 8501 already in use
```bash
streamlit run app.py --server.port=8502
```

---

## 📦 Project Structure

```
AI IT Support Agent/
├── app.py                    # Main Streamlit app (~400 lines)
├── test_app.py              # Unit tests (33 tests)
├── test_streamlit_ui.py      # UI tests (25 tests)
├── conftest.py              # pytest config
├── requirements.txt         # Python dependencies
├── requirements-dev.txt     # Dev dependencies
├── Dockerfile               # Docker config
├── docker-compose.yml       # Docker compose
├── .streamlit/config.toml   # Streamlit config
├── .env.example             # API key template
├── Procfile                 # Dewacloud entry
└── README.md                # This file
```

---

## 📋 Dependencies

### Production (requirements.txt)
```
streamlit>=1.42.0              # Web UI framework
google-generativeai>=0.5.0     # Gemini API client
python-dotenv==1.0.0          # Environment variables
requests==2.31.0              # HTTP library
protobuf>=4.25.0              # Python 3.14 compatibility
```

### Development (requirements-dev.txt)
```
pytest==7.4.3                 # Testing framework
pytest-mock==3.12.0           # Mocking support
pytest-cov==4.1.0             # Coverage reporting
```

---

## 🔐 Security Best Practices

✅ **DO**:
- Keep `.env` file LOCAL only (never commit to git)
- Use Dewacloud's secure environment variables
- Enable HTTPS (Dewacloud default)
- Rotate API keys regularly

❌ **DON'T**:
- Commit `.env` to repository
- Share API keys in chats/emails
- Hard-code secrets in app.py
- Use deprecated dependency versions

---

## 🐳 Docker (Optional - Local Testing)

```bash
# Build image
docker build -t ai-it-support:latest .

# Run with API key
docker run -p 8501:8501 \
  -e GEMINI_API_KEY=your_key \
  ai-it-support:latest

# Or use docker-compose
docker-compose up --build
```

Access at: `http://localhost:8501`

---

## 📞 Resources & Links

| Resource | Link |
|----------|------|
| Gemini API Docs | https://ai.google.dev |
| Streamlit Docs | https://docs.streamlit.io |
| Dewacloud Dashboard | https://dashboard.dewacloud.com |
| Repository | https://github.com/fitrifitriah/AI-IT-Support-Agent-vb |

---

## 📄 License

This project is created for interview showcase and demonstration purposes.

---

**Made with ❤️** | Version 1.0.0 | May 25, 2026
