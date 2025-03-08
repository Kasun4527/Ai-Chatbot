from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(dotenv_path="Chatbot/.env")

 # Add this line to check if the key is loaded properly


# Retrieve the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

print("Loaded API Key:", api_key) 

# Check if the API key is loaded correctly
if not api_key:
    print("API key is not loaded properly!")
else:
    print("API key loaded successfully!")

# Set the OpenAI API key
openai.api_key = api_key

# Initialize FastAPI app
app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.post("/chat")
async def chat(input: dict):
    print("Received message:", input["message"])  # Debugging log
    
    try:
        # Sending request to OpenAI with the correct method for gpt-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Correct model name for chat-based completions
            messages=[{"role": "user", "content": input["message"]}],  # Pass the message as part of the conversation
        )

        # Get the chatbot's reply from the response
        chatbot_reply = response["choices"][0]["message"]["content"].strip()  # Extract the content of the response

        print(f"Chatbot reply: {chatbot_reply}")  # Debugging log
        return {"response": chatbot_reply}  # Return the response as JSON

    except Exception as e:
        print("Error in OpenAI API:", e)  # Log any errors
        return {"response": "Error processing request"}  # Handle errors gracefully
