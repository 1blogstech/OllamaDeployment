from flask import Flask, render_template, request, jsonify
import chatbot
import datetime


class Ollama_App():
    def __init__(self):
        self.app = Flask(__name__,template_folder="templates")
        @self.app.route('/')
        def main_page():
            time_ = datetime.datetime.strftime(datetime.datetime.now(), "%H:%M")
            return render_template("index.html",time=time_)

        @self.app.route('/chat', methods=['POST'])
        def chat_with_ollama():
            data = request.json  # Get JSON data from frontend
            user_message = data.get("message")# Get user's message
            ollama = chatbot.handle_conversation(user_message)
            time_ = datetime.datetime.strftime(datetime.datetime.now(),"%H:%M")
            data = str(ollama)
            return jsonify({"response": data,"time":time_})


    def run(self):
        self.app.run(host="0.0.0.0")

if __name__ == "__main__":
    app_runner = Ollama_App()
    app_runner.run()