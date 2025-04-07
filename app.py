from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/debug")
def debug():
    return "This is the debug route. Everything's (hopefully) fine."


@app.route("/about")
def about():
    return "This is a simple Flask app."


if __name__ == "__main__":
    app.run(debug=True)
