from flask import Flask
from database import get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    conn = get_db_connection()
    conn.close()
    return "FocusLens Database Connection Successful"

if __name__ == "__main__":
    app.run(debug=True)
