# AI & Machine Learning Tutor Chatbot

## Project Description

This project is an AI-powered chatbot designed to help beginners learn Python, NumPy, Pandas, Machine Learning, Deep Learning, and Artificial Intelligence.

The application uses a Streamlit frontend, FastAPI backend, and a Hugging Face AI model.

## Technologies Used

* Python
* Streamlit
* FastAPI
* Pydantic
* Requests
* Hugging Face Inference API

## Project Structure

* `chatbot.py` — Contains the chatbot and AI model logic.
* `api.py` — FastAPI backend and `/chat` API endpoint.
* `app.py` — Streamlit user interface.
* `main.py` — Terminal-based chatbot interface.
* `requirements.txt` — Required Python packages.

## How to Run

### 1. Activate the virtual environment

```text
venv\Scripts\activate
```

### 2. Start FastAPI

```text
uvicorn api:app --reload
```

### 3. Start Streamlit in another terminal

```text
streamlit run app.py
```

### 4. Open the Streamlit application

Use the URL displayed in the terminal, normally:

```text
http://localhost:8501
```

## Features

* AI-powered conversational tutoring
* Python and Machine Learning explanations
* Conversation history
* Clear chat functionality
* FastAPI REST API
* Streamlit graphical interface
* Error handling
