import openai
import gradio as gr
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API key from the environment variable
openai.api_key = api_key

messages = [{"role": "system", "content": "You are a financial expert that specializes in real estate investment and negotiation"}]

def custom_chatgpt(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    chatgpt_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": chatgpt_reply})
    return chatgpt_reply

# Create a Gradio interface
demo = gr.Interface(fn=custom_chatgpt, inputs="text", outputs="text", title="Real Estate Pro")

# Launch the application with sharing options
demo.launch(share=True)
