from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Backend Engineer',
        'location': 'San Francisco USA',
        'salary': '$1100'
    },
    {
        'id': 2,
        'title': 'UX/UI Engineer',
        'location': 'Texas USA',
        'salary': '$1500'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'remote'
    },
    {
        'id': 4,
        'title': 'AI Engineer',
        'location': 'Washington USA',
        'salary': '$2000'
    },

]


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS, company_name="Hoang")


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
