from flask import Flask
import pandas as pd

print("Hello")

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello"

if __name__ == "__main__":
    app.run()

