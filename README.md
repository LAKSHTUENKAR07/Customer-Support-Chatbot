# 📞 Telecom Customer Support Chatbot 🤖

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API%20Backend-green.svg)](https://fastapi.tiangolo.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-lightgrey.svg)](https://platform.openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A web-based **customer support chatbot** for telecom services built using **FastAPI** and **OpenAI GPT-4**. The chatbot simulates a helpful support agent capable of handling common customer issues like connectivity, billing, and more.

---

## 🌟 Features

- 🔍 **AI-powered responses** using GPT-4
- 🖥️ **Frontend chat UI** with clean HTML/CSS interface
- ⚡ **FastAPI backend** for message processing
- 🔁 **User feedback system** (thumbs up/down)
- 🔐 **Environment-secured API key** with `.env`
- 🌍 **CORS-enabled** for smooth frontend-backend communication

---

## 📂 Project Structure

| File | Purpose |
|------|---------|
| `index.html` | Frontend chat interface |
| `main.py` | FastAPI backend API using OpenAI |
| `.env` | Stores API key (`OPENAI_API_KEY`) |
| `requirements.txt` | List of Python dependencies |

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/telecom-chatbot.git
cd telecom-chatbot

### 2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Set OpenAI API Key
Create a .env file in the root directory:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_api_key
4. Run the Backend
bash
Copy
Edit
uvicorn main:app --reload
5. Launch Frontend
Simply open index.html in your web browser.

🌐 Deployment (Optional)
You can deploy the backend using platforms like:

Render

Railway

Heroku

And serve the frontend via:

GitHub Pages

Vercel

Netlify

📜 License
This project is licensed under the MIT License.

🙌 Acknowledgements
OpenAI

FastAPI

Uvicorn
