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


@app.route("/get_products")
def get_products():
    return render_template("products.html",
                           products=mongo.db.products.find())


@app.route("/add_production")
def add_production():
    return render_template("addproduction.html",
                           employees=mongo.db.employees.find(),
                           products=mongo.db.products.find(),
                           machines=mongo.db.machines.find())


@app.route("/insert_production", methods=["POST"])
def insert_production():
    productions = mongo.db.productions
    productions.insert_one(request.form.to_dict())
    return redirect(url_for("get_productions"))


@app.route("/add_product")
def add_product():
    return render_template("addproduct.html",
                           products=mongo.db.products.find())


@app.route("/insert_product", methods=["POST"])
def insert_product():
    products = mongo.db.products
    products.insert_one(request.form.to_dict())
    return redirect(url_for("get_products"))


@app.route('/register_production/<production_id>')
def register_production(production_id):
    the_production = mongo.db.productions.find_one({"_id": ObjectId(production_id)})
    all_employees = mongo.db.employees.find()
    return render_template('registerproduction.html',
                           production=the_production,
                           employees=all_employees)


@app.route('/edit_production/<production_id>')
def edit_production(production_id):
    the_production = mongo.db.productions.find_one({"_id": ObjectId(production_id)})
    all_employees = mongo.db.employees.find()
    all_machines = mongo.db.machines.find()
    all_products = mongo.db.products.find()
    return render_template('editproduction.html', production=the_production,
                           employees=all_employees, machines=all_machines,
                           products=all_products)


@app.route("/update_production/<production_id>", methods=["GET", "POST"])
def update_production(production_id):
    productions = mongo.db.productions
    productions.update({"_id": ObjectId(production_id)},
    {
         'product_number': request.form.get('product_number'),
         'product_name': request.form.get('product_name'),
         'machine_name': request.form.get('machine_name'),
         'employees': request.form.getlist('employees[]'),
         'comments': request.form.get('comments'),
         'date': request.form.get('date')
    })
    return redirect(url_for("get_productions"))


@app.route('/delet_production/<production_id>')
def delet_production(production_id):
    mongo.db.productions.remove({"_id": ObjectId(production_id)})
    return redirect(url_for("get_productions"))


@app.route('/delet_product/<product_id>')
def delet_product(product_id):
    mongo.db.products.remove({"_id": ObjectId(product_id)})
    return redirect(url_for("get_products"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
