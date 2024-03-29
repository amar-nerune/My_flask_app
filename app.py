from flask import Flask, render_template, jsonify
from database import engine
import pymysql

from sqlalchemy import create_engine, text


app = Flask(__name__)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        item = result.mappings().all()
        # print(result.mappings().all())
        result_dicts = []
        for val in item:
            result_dicts.append(dict(val))
        return result_dicts

@app.route("/")
def myfunc():
    JOBS = load_jobs_from_db()
    return render_template("home.html", jobs =JOBS, company_name="Amtech")

@app.route("/api/jobs")
def list_jobs():
    JOBS = load_jobs_from_db()
    return jsonify(JOBS)
    

if __name__=="__main__":
    app.run(debug=True)
