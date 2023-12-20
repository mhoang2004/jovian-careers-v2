from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, add_application_to_db

app = Flask(__name__)

COMPANY_NAME = "Hoang"


@app.route("/")
def home_page():
    jobs = load_jobs_from_db()
    return render_template("home.html", style_file="home", jobs=jobs, company_name=COMPANY_NAME)


@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
    jobs = load_jobs_from_db(id)
    if not jobs:
        return "Not Found", 404
    return render_template("job-page.html", style_file="job-page", jobs=jobs, company_name=COMPANY_NAME)


@app.route("/api/job/<id>")
def show_api_job(id):
    jobs = load_jobs_from_db(id)
    return jsonify(jobs)


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
    data = request.form
    jobs = load_jobs_from_db(id)

    add_application_to_db(id, data)
    return render_template("application-submitted.html", style_file="application", data=data, jobs=jobs, company_name=COMPANY_NAME)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
