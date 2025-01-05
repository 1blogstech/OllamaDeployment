from flask import Flask, render_template, request, jsonify
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import datetime

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation(user_input):
    context = ""
    result = chain.invoke({"context":context,"question":user_input})
    context = f"\nUser: {user_input}\nAI: {result}"
    return result

app = Flask(__name__, template_folder="templates")

@app.route('/')
def main_page():
    time_ = datetime.datetime.strftime(datetime.datetime.now(), "%H:%M")
    return render_template("index.html", time=time_)

@app.route('/chat', methods=['POST'])
def chat_with_ollama():
    data = request.json  # Get JSON data from frontend
    user_message = data.get("message")  # Get user's message
    ollama = handle_conversation(user_message)
    time_ = datetime.datetime.strftime(datetime.datetime.now(), "%H:%M")
    data = str(ollama)
    return jsonify({"response": data, "time": time_})
