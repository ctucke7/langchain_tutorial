# langchain_quickstart.py

import os, getpass
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

# Load .env file if it exists
load_dotenv()

# Enable LangSmith tracing
os.environ["LANGSMITH_TRACING"] = "true"

# Ask for your keys if not already set
if "LANGSMITH_API_KEY" not in os.environ:
    os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")

if "LANGSMITH_PROJECT" not in os.environ:
    os.environ["LANGSMITH_PROJECT"] = "default"

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google Gemini API key: ")

# Initialize Gemini model
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

# Create messages
messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

# Run model
response = model.invoke(messages)

print("Model response:", response)
