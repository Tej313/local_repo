import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")

while True:
    user_input = input("You (type 'quit()' to exit): ")
    if user_input == "quit()":
        break
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
