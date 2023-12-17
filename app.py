from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)


@app.route("/")
def home_page():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs, company_name="Hoang")


@app.route("/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
