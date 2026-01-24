from flask import Flask, render_template
from database import initialize_database

app = Flask(__name__)

initialize_database()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)