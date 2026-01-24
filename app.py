from flask import Flask, render_template, request, redirect
from database import initialize_database, insert_session

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

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)