import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)


app.config["MONGO_DBNAME"] = "Production_Management"
app.config["MONGO_URI"] = "mongodb+srv://ninos77:Itanaeliana1216@myfirstcluster-fsr8d.mongodb.net/Production_Management?retryWrites=true&w=majority"

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_productions")
def get_productions():
    return render_template("productions.html",
                           productions=mongo.db.productions.find(),
                           employees=mongo.db.employees.find())


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
