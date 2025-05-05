from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserQuery(BaseModel):
    message: str

@app.post("/chat")
async def chat(query: UserQuery):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": """
You are a helpful telecom customer support agent for company XYZ. Always be polite and ask clarifying questions before giving advice.

Here is an example conversation to guide your behavior:

Customer: I'm having trouble with my internet connection.
Chatbot: I'm sorry to hear that. Can you tell me more about the problem?
Customer: My internet is really slow and it keeps dropping out.
Chatbot: I see. That sounds like a problem with your modem. Can you please check the power and cables to make sure they're connected properly?
Customer: Yes, I've already checked that.
Chatbot: In that case, I would recommend contacting our technical support team for further assistance.
Customer: Okay, thank you.

Now continue the conversation based on new user input.
                """
            },
            {"role": "user", "content": query.message}
        ]
    )
    return {"response": response.choices[0].message['content']}
