# AI Image Recognition Chatbot

An AI-powered chatbot built with **Flask** and **Google Gemini 1.5 Flash** that supports both text conversations and image-based landmark recognition. Users can chat naturally with the bot or upload an image to identify landmarks and Indian temples with their locations.

## Features

* AI-powered conversational chatbot using Gemini 1.5 Flash.
* Image upload and landmark recognition.
* Indian temple identification with location details.
* Clean and responsive chat interface.
* Real-time responses using Flask APIs.

## Tech Stack

* **Backend:** Flask (Python)
* **AI Model:** Google Gemini 1.5 Flash
* **Frontend:** HTML, CSS, JavaScript
* **Image Processing:** Pillow
* **API:** Google Generative AI

## Project Structure

* `app.py` – Flask backend and Gemini API integration.
* `index.html` – Chatbot user interface.
* `requirements.txt` – Project dependencies.
* `README.md` – Project documentation.

## Installation

1. Clone the repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your Gemini API key in `app.py`.
4. Run the application:

```bash
python app.py
```

5. Open `http://127.0.0.1:5000` in your browser.

## Future Improvements

* Chat history support.
* Voice input and speech responses.
* Multi-language conversations.
* More accurate landmark recognition with confidence scores.
