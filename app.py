# import necessary libraries
import os
import pandas as pd
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
SQLALCHEMY_TRACK_MODIFICATEION = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Project2.db"
db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)

Redfin = Base.classes.redfin_aug2019
Divvy_stationinfo = Base.classes.divvy_stationinfo
Divvy_stationstatus = Base.classes.divvy_stationstatus

@app.route("/")
def home_page():
    return render_template("index.html")


# @app.route("/")
# # Steve


@app.route("/Redfin")
def Redfin():
    select = [Redfin.Neighborhood, 
    Redfin.Lat, 
    Redfin.Lng, 
    Redfin.Sale_Price, 
    Redfin.Homes_Sold,
    Redfin.New_Listings,
    Redfin.Days_on_Market]

    results = db.session.query(*select).all()
    print(results)

    return "Success"


@app.route("/DivvyStationInfo")
def DivvyInfo():
    select = [Divvy_stationinfo.lat, 
    Divvy_stationinfo.lon, 
    Divvy_stationinfo.name, 
    Divvy_stationinfo.station_id]

    results = db.session.query(*select).all()
    print(results)

    return "Success"

@app.route("/DivvyStationStatus")
def DivvyInfo():
    select = [Divvy_stationstatus.is_installed, 
    Divvy_stationstatus.num_docks_available, 
    Divvy_stationstatus.num_ebikes_available, 
    Divvy_stationstatus.station_id]

    results = db.session.query(*select).all()
    print(results)

    return "Success"

# @app.route("/")
# # Rachel


# @app.route("/api/table_analysis")
# def table_analysis():
#     results = pd.read_sql("SELECT * from divvy_stationinfo", con=db.engine)
#     csv_results = results.to_csv()
#     return csv_results


if __name__ == "__main__":
    app.run(debug=True)
