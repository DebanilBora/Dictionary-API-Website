from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # Get the 'word' from query string (GET request)
    word = request.args.get("word", "")
    result = {}

    if request.method == "POST":
        # If form is submitted, grab the word and redirect to GET route
        word = request.form.get("word", "").strip()
        if word:
            return redirect(url_for("index", word=word))  # Redirect to avoid re-submission

    if word:  # If there's a word in the URL, fetch its meaning
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json()[0]
            result = {
                "word": data.get("word"),
                "phonetic": data.get("phonetic"),
                "phonetics": data.get("phonetics", []),
                "meanings": data.get("meanings", [])
            }
        else:
            result["error"] = "Word not found"

    return render_template("index.html", word=word, result=result)

if __name__ == "__main__":
    app.run(debug=True)
