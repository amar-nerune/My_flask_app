from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [     {
    "id":1,
    "title": 'Data analyst',
    'location':"pune",
    "salary": "15 lacks"
},
{
    "id":1,
    "title": 'Data Scintist',
    'location':"pune",
    "salary": "15 lacks"
},
{
    "id":1,
    "title": 'Data Engineer',
    'location':"pune",
    "salary": "15 lacks"
}
]

@app.route("/")
def myfunc():
    return render_template("home.html", jobs =JOBS, company_name="Amtech")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
    

if __name__=="__main__":
    app.run(debug=True)
