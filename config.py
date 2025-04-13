import os

SENTIMENT_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"
CHATBOT_MODEL = "microsoft/DialoGPT-medium"


# ===============================
# 🔎 Flask Configuration
# ===============================
class FlaskConfig:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'supersecretkey')

# ===============================
# 📅 Google Calendar API Configuration
# ===============================
class GoogleCalendarConfig:
    # Path to the service account JSON file
    CREDENTIALS_FILE = os.environ.get('GOOGLE_CREDENTIALS_FILE', 'credentials.json')
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    # Calendar ID (You can use 'primary' for your default calendar)
    CALENDAR_ID = os.environ.get('GOOGLE_CALENDAR_ID', 'primary')

# ===============================
# 📝 Task Manager Configuration
# ===============================
class TaskManagerConfig:
    # Path to store tasks locally
    TASK_FILE = os.environ.get('TASK_FILE', 'tasks.json')
    CHECK_INTERVAL = 60  # Check tasks every 60 seconds

# ===============================
# 📊 Logging Configuration
# ===============================
class LoggingConfig:
    LOG_FILE = os.environ.get('LOG_FILE', 'app.log')
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')

# ===============================
# 🔎 Overall Configuration
# ===============================
class Config(FlaskConfig, GoogleCalendarConfig, TaskManagerConfig, LoggingConfig):
    pass
