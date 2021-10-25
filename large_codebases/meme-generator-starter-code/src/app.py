"""Module that defines a Flask web application."""
import random
import os
import requests
from flask import Flask, render_template, request, flash, redirect, url_for

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)
app.secret_key = "random  key"
meme = MemeEngine("./static")


def setup():
    """Load all resources."""
    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]

    quotes = []
    for quote_file in quote_files:
        if Ingestor.can_ingest(quote_file):
            quotes.extend(Ingestor.parse(quote_file))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information."""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme."""
    try:
        image_url = request.form.get("image_url")
        r = requests.get(image_url, stream=True)
    except requests.exceptions.RequestException:
        flash("Enter a valid URL address.")
        return redirect(url_for("meme_form"))

    if not os.path.exists("./tmp"):
        os.mkdir("./tmp")
    img_path = f"./tmp/{random.randint(0, 100000000)}.png"
    with open(img_path, "wb") as file:
        file.write(r.content)

    body = request.form.get("body")
    author = request.form.get("author")
    if not (author and body):
        flash("Don't forget to enter a quote and an author.")
        return redirect(url_for("meme_form"))

    try:
        meme_path = meme.make_meme(img_path, body, author)
    except Exception as e:
        print(e)
        flash("Invalid data entered.")
        if os.path.exists(img_path):
            os.remove(img_path)
        return redirect(url_for("meme_form"))

    if os.path.exists(img_path):
        os.remove(img_path)

    return render_template("meme.html", path=meme_path)


if __name__ == "__main__":
    app.run()
