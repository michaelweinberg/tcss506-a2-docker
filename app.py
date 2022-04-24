from flask import Flask, render_template, request
from datetime import datetime as dt

app = Flask(__name__)

@app.route("/owner")
def owner():
    return "Hello World from Michael Weinberg"

@app.route("/datetime")
def datetime():
    return dt.now().strftime("%d/%m/%Y %H:%M:%S")

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

