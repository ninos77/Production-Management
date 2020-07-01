import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

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


@app.route("/update_production/<production_id>", methods=["POST"])
def update_production(production_id):
    productions = mongo.db.productions
    productions.update({"_id": ObjectId(production_id)},
    {
         'product_name': request.form.get('product_name'),
         'machine_name': request.form.get('machine_name'),
         'product_number': request.form.get('product_number'),
         'employees': request.form.get('employees'),
         'comments': request.form.get('comments'),
         'date': request.form.get('date')
    })
    return redirect(url_for("get_productions"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
