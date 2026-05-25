# 🚀 Quick Start: Deploy to Dewacloud

## 📦 Files Created for Deployment

```
AI IT Support Agent/
├── Dockerfile                    # Container configuration
├── docker-compose.yml            # Local testing with Docker
├── .streamlit/config.toml        # Streamlit settings
├── .dockerignore                 # Files to exclude from Docker build
├── DEPLOYMENT_GUIDE.md           # Complete deployment documentation
└── .env                          # API keys (keep secure!)
```

## ⚡ Quick Deploy (5 Minutes)

### Step 1: Push to Git Repository

```bash
# Initialize git if not already
git init
git config user.email "your-email@example.com"
git config user.name "Your Name"

# Add all files except .env
git add -A
git commit -m "Initial AI IT Support Agent - ready for deployment"

# Push to your repository
git remote add origin https://your-repo-url.git
git push -u origin main
```

**Important:** Make sure `.env` is in `.gitignore` (already done ✓)

### Step 2: Deploy on Dewacloud Dashboard

1. **Login** to [Dewacloud Dashboard](https://dashboard.dewacloud.com)
2. Click **"New App"** → **"Docker"**
3. Select **"Git Repository"** as source
4. Paste your repository URL
5. Configure:
   - **Dockerfile Path**: `Dockerfile`
   - **Build Command**: (leave blank)
   - **Port**: `8501`

### Step 3: Set Environment Variables

In Dewacloud dashboard → **Environment Variables**:

```
![alt text](image.png)=
```

### Step 4: Deploy!

Click **"Deploy"** button and wait 3-5 minutes ✨

---

## 🧪 Test Locally Before Deploying

```bash
# Build Docker image
docker build -t ai-it-support:latest .

# Run with environment variables
docker run -p 8501:8501 \
  -e GEMINI_API_KEY= \
  ai-it-support:latest

# Or use docker-compose (simpler)
docker-compose up --build
```

Then visit: `http://localhost:8501`

---

## 🔐 Security Checklist

✅ `.env` file is in `.gitignore`  
✅ API key is set in Dewacloud secrets, not in code  
✅ CORS is disabled (only for your domain)  
✅ HTTPS is enabled (Dewacloud provides this)  

**NEVER commit `.env` to repository!**

---

## 📊 After Deployment

### Access Your App

- **URL**: `https://your-app-name.dewacloud.id`
- Share this URL with users

### Monitor Performance

In Dewacloud dashboard:
- **Logs** → View application output
- **Metrics** → CPU, Memory, Network usage
- **Status** → Check if app is running

### View Logs

```bash
# If using Dewacloud CLI:
dewacloud logs your-app-name

# Or check directly in dashboard
```

---

## 🔄 Update & Redeploy

1. Make changes locally
2. Test with `docker-compose up`
3. Push to Git: `git push origin main`
4. Dewacloud auto-deploys (if configured)

Or manually redeploy in Dewacloud dashboard

---

## ❌ Troubleshooting

### App won't start

```bash
# Check logs in Dewacloud dashboard
# Look for errors like:
# - "GEMINI_API_KEY not found" → Add environment variable
# - "Port already in use" → Change port in dockerfile
# - "Module not found" → requirements.txt issue
```

### API errors

```bash
# Test API key locally
python -c "
import google.generativeai as genai
genai.configure(api_key='YOUR_KEY')
print(genai.list_models())
"
```

### Build failures

```bash
# Test Docker build locally first
docker build -t test:latest .

# If it fails, debug with:
docker build --progress=plain -t test:latest .
```

---

## 📞 Support

| Topic | Link |
|-------|------|
| Dewacloud Docs | https://docs.dewacloud.com |
| Streamlit Docs | https://docs.streamlit.io |
| Gemini API | https://ai.google.dev |
| Docker Docs | https://docs.docker.com |

---

## 📝 Production Deployment Checklist

Before deploying to production:

- [ ] Test locally with `docker-compose up`
- [ ] All tests pass: `pytest -v`
- [ ] Environment variables configured in Dewacloud
- [ ] `.env` file is in `.gitignore`
- [ ] Repository is public or deploy key is configured
- [ ] Health checks are enabled
- [ ] Logging is configured
- [ ] SSL/HTTPS is enabled (Dewacloud default)
- [ ] Auto-restart is enabled
- [ ] Monitoring dashboard is open

---

## 🎉 You're Ready!

Your AI IT Support Agent is now:
- ✅ Containerized (Docker)
- ✅ Ready for cloud deployment
- ✅ Secure with environment variables
- ✅ Monitored and logged
- ✅ Auto-scaling capable

**Happy Deploying!** 🚀
