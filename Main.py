from flask import Flask, render_template
# import pandas as pd

# print("Hello")

app = Flask(__name__, static_folder="static")

@app.route('/')
def home():
    return render_template('index_copy.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

