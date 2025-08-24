# 📖 Flask Dictionary Web App

A simple Flask web application that allows users to search for English words and get their meanings, phonetics, and usage using the [Free Dictionary API](https://dictionaryapi.dev/).

🌐 **Live Demo:** [https://dictionary-api-website.onrender.com/](https://dictionary-api-website.onrender.com/)

## 🚀 Features
- Search for English words
- Displays phonetic spelling and pronunciation links (if available)
- Shows word meanings and part of speech
- Handles invalid or unknown words gracefully

## 🛠️ Tech Stack
- Python 3
- Flask
- Requests
- HTML (Jinja2 templates)

## 📂 Project Structure
.
├── app.py # Main Flask app
├── templates/
│ └── index.html # Frontend template
├── requirements.txt # Dependencies
└── README.md # Documentation


## ⚙️ Installation & Setup

1. Clone the repository
   ```bash
   git clone https://github.com/DebanilBora/Dictionary-API-Website.git
   cd flask-dictionary-app
2.Create and activate a virtual environment
  python -m venv .venv
  source .venv/bin/activate   # On Linux/Mac
  .venv\Scripts\activate      # On Windows
3.Install dependencies
  pip install -r requirements.txt
4.Run the Flask server
  python app.py
5.Open in your browser
  http://127.0.0.1:5000/
  📦 Requirements
Create a requirements.txt with:
Flask==3.0.3
Flask-Bootstrap==3.3.7.1
Flask-WTF==1.2.2
WTForms==3.2.1
requests==2.32.4
gunicorn==23.0.0

✨ Example Usage
Search for the word: hello

Output: Phonetic spelling + multiple meanings
🏷️ Tags

Flask Python API Dictionary WebApp Bootstrap Requests REST Frontend Backend WebDevelopment
