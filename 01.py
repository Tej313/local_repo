import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API key from the environment variable
openai.api_key = api_key

# Create a chat completion request
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "write essay about penguins"}]
)

# Print the response from the model
print(completion.choices[0].message.content)
