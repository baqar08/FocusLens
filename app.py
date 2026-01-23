from flask import Flask
from database import initialize_database

app = Flask(__name__)

initialize_database()

@app.route("/")
def home():
    return "FocusLens backend running"

if __name__ == "__main__":
    app.run(debug=True)