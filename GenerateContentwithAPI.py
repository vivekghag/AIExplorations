from dotenv import load_dotenv
import os
from google import genai

# Load environment variables from the .env file
load_dotenv()

# Access the GEMINI_API_KEY
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini client
client = genai.Client(api_key=api_key)

# Example usage
print(f"Your GEMINI_API_KEY is: {api_key}")

# Example: Make your first request
# Modify the request to generate content for a specific query
query = "Which are top 5 economies in the world?"
response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=query
)

# Print the response
print("Query:", query)
print("Response from Gemini API:", response)