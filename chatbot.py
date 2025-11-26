from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.0-flash")

print("\n🤖 Gemini Chatbot Ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye 👋")
        break

    response = model.generate_content(
        contents=[{"role": "user", "parts": [{"text": user_input}]}]
    )

    print("Bot:", response.text)
