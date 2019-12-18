# import necessary libraries
from sqlalchemy import func

from flask import Flask, render_template, jsonify, request, redirect

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
SQLALCHEMY_TRACK_MODIFICATEION = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Project2.db.sqlite"
db = SQLAlchemy(app)


Base = automap_base()
Base.prepare(db.engine, reflect=TRUE)


@app.route("/")
def home_page():
    return render_template("index,html")


@app.route("/")
# Steve


@app.route("/")
# Pamela


@app.route("/")
# Rachel


@app.route("/api/table_analysis")
def table_analysis():
    results = pd.read_sql("SELECT * from divvy_stationinfo", con=db.engine)
    csv_results = results.to_csv()
    return csv_results


if __name__ == "__main__":
    app.run(debug=True)
