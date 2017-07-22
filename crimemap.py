
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 16:09:17 2017

@author: Mateusz
"""

from dbhelper import DBHelper
from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask(__name__)
DB = DBHelper()


@app.route("/")
def home():
     crimes = DB.get_all_crimes()
     crimes = json.dumps(crimes)
     return render_template("home.html", crimes=crimes)


@app.route("/submitcrime",methods=["POST"])
def submitcrime():
    category = request.form.get("category")
    date = request.form.get("date")
    latitude = float(request.form.get("latitude"))
    longitude = float(request.form.get("longitude"))
    description = request.form.get("description")
    DB.add_crime(category, date, latitude, longitude, description)
    return home()



if __name__ == "__main__":
    app.run(port=5003, debug=True)