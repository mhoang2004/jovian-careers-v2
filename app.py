from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)


@app.route("/")
def home_page():
    jobs = load_jobs_from_db()
    return render_template("home.html", style_file="home", jobs=jobs, company_name="Hoang")


@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
    jobs = load_jobs_from_db(id)
    if not jobs:
        return "Not Found", 404
    return render_template("jobpage.html", style_file="jobpage", jobs=jobs, company_name="Hoang")


@app.route("/api/job/<id>")
def show_api_job(id):
    jobs = load_jobs_from_db(id)
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
