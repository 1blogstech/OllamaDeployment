from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

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

if __name__ == "__main__":
    print(handle_conversation("hi"))
