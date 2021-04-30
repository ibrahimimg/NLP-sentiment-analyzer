from flask import Flask, render_template, url_for, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    text = ""
    if request.method == "POST":
        text = request.form['text']
        polarity, subjectivity = TextBlob(text).sentiment
        result = ""
        if polarity>0:
            result = "Positive"
        elif polarity<0:
            result = "Negative"
        else:
            result = "Neutral"

        return render_template("index.html",
            text = text,
            confidence = round(abs(polarity*100)),
            result = result)

    return render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug=False)
