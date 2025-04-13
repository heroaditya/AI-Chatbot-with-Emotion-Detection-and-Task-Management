from flask import Flask, request, render_template, jsonify, send_file
from models.sentiment_model import SentimentAnalyzer
from models.chatbot_model import Chatbot
from models.calendar_model import CalendarModel
from task_manager import TaskManager
from datetime import datetime

# Initialize app and models
app = Flask(__name__)
sentiment_analyzer = SentimentAnalyzer()
chatbot_model = Chatbot()
calendar_model = CalendarModel()
task_manager = TaskManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')
    
    if not user_input:
        return jsonify({"response": "Please enter a message!"})

    # Sentiment Analysis
    sentiment = sentiment_analyzer.analyze_sentiment(user_input)

    # Task Management
    if "remind me" in user_input.lower():
        task_manager.add_task(user_input)
        return jsonify({"response": "Reminder set successfully!"})

    elif "schedule a meeting" in user_input.lower():
        details = user_input.replace("schedule a meeting", "").strip()
        if details:
            start_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            end_time = (datetime.now().replace(hour=datetime.now().hour + 1)).strftime("%Y-%m-%dT%H:%M:%S")
            
            file_name = calendar_model.create_event(
                summary="Meeting",
                description=details,
                start_time=start_time,
                end_time=end_time
            )
            return jsonify({"response": "Meeting scheduled! Download your .ics file:", "file": file_name})
        else:
            return jsonify({"response": "Please provide meeting details."})

    # Chatbot Response Generation
    chatbot_response = chatbot_model.generate_response(user_input)
    
    # Formulate Response based on Sentiment
    if sentiment == "positive":
        final_response = f"😊 {chatbot_response}"
    elif sentiment == "negative":
        final_response = f"😔 {chatbot_response}"
    else:
        final_response = f"😐 {chatbot_response}"

    return jsonify({"response": final_response})

@app.route('/download_ics', methods=['GET'])
def download_ics():
    file_name = 'meeting_event.ics'
    try:
        return send_file(file_name, as_attachment=True)
    except FileNotFoundError:
        return jsonify({"error": "No event found to download."})

if __name__ == '__main__':
    app.run(debug=True)
