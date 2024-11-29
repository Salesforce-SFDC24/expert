import openai
import json
import os

# OpenAI API key (replace with your actual key)
openai.api_key = "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"
# Session context for maintaining conversation history
session_context = []

# File to save logs
LOG_FILE = "assistant_logs.json"

def save_logs():
    """Save session context to a log file."""
    with open(LOG_FILE, "w") as log_file:
        json.dump(session_context, log_file, indent=4)

def load_logs():
    """Load session context from a log file."""
    global session_context
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as log_file:
            session_context = json.load(log_file)

def gpt4_response(query):
    """
    Sends a query to OpenAI GPT-4 and returns the response.
    """
    try:
        # Add user query to the session context
        session_context.append({"role": "user", "content": query})
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=session_context
        )
        # Extract response and append to session context
        assistant_response = response['choices'][0]['message']['content']
        session_context.append({"role": "assistant", "content": assistant_response})
        return assistant_response
    except Exception as e:
        return f"Error with GPT-4 API: {e}"

def run_assistant_with_gpt():
    """
    A command-line interface for interacting with the assistant.
    """
    print("Welcome to your GPT-4 Assistant! Type 'exit' to quit.")
    print("Type 'save' to save logs or 'load' to load logs.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Assistant: Goodbye!")
            break
        elif user_input.lower() == "save":
            save_logs()
            print("Assistant: Logs saved successfully.")
            continue
        elif user_input.lower() == "load":
            load_logs()
            print("Assistant: Logs loaded successfully.")
            continue
        response = gpt4_response(user_input)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    run_assistant_with_gpt()