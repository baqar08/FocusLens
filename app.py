from flask import Flask, render_template, request, redirect
from database import initialize_database, insert_session, fetch_sessions
from utils.analysis import analyze_sessions

app = Flask(__name__)

initialize_database()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        session_date = request.form.get("session_date")
        time_period = request.form.get("time_period")
        duration = request.form.get("duration")
        energy_level = request.form.get("energy_level")
        task_type = request.form.get("task_type")

        insert_session(session_date, time_period, duration, energy_level, task_type)
        return redirect("/")

    sessions = fetch_sessions()
    insights = analyze_sessions(sessions)

    return render_template("index.html", sessions=sessions, insights=insights)

if __name__ == "__main__":
    app.run(debug=True)