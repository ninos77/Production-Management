import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config.from_object("config.DevelopmentConfig")

mongo = PyMongo(app)


# -------Production(CRUD)-------------
@app.route("/")
@app.route("/get_productions")
def get_productions():
    print(app.config["ENV"])
    return render_template("productions.html",
                           productions=mongo.db.productions.find(),
                           employees=mongo.db.employees.find())


@app.route("/add_production")
def add_production():
    return render_template("addproduction.html",
                           products=mongo.db.products.find(),
                           machines=mongo.db.machines.find())


@app.route("/insert_production", methods=["POST"])
def insert_production():
    productions = mongo.db.productions
    productions.insert_one(request.form.to_dict())
    return redirect(url_for("get_productions"))


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
         'employees': request.form.getlist('employees'),
         'comments': request.form.get('comments'),
         'date': request.form.get('date')
    })
    return redirect(url_for("get_productions"))


@app.route('/delet_production/<production_id>')
def delet_production(production_id):
    mongo.db.productions.remove({"_id": ObjectId(production_id)})
    return redirect(url_for("get_productions"))

# -------Product(CRUD)-------------
@app.route("/get_products")
def get_products():
    return render_template("products.html",
                           products=mongo.db.products.find())


@app.route("/add_product")
def add_product():
    return render_template("addproduct.html")


@app.route("/insert_product", methods=["POST"])
def insert_product():
    products = mongo.db.products
    products.insert_one(request.form.to_dict())
    return redirect(url_for("get_products"))


@app.route('/edit_product/<product_id>')
def edit_product(product_id):
    the_product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    return render_template('editproduct.html', product=the_product)


@app.route("/update_product/<product_id>", methods=["GET", "POST"])
def update_product(product_id):
    products = mongo.db.products
    products.update({"_id": ObjectId(product_id)},
    {
         'product_name': request.form.get('product_name')
    })
    return redirect(url_for("get_products"))


@app.route('/delet_product/<product_id>')
def delet_product(product_id):
    mongo.db.products.remove({"_id": ObjectId(product_id)})
    return redirect(url_for("get_products"))

# -------Machine(CRUD)-------------
@app.route("/get_machines")
def get_machines():
    return render_template("machines.html",
                           machines=mongo.db.machines.find())


@app.route("/add_machine")
def add_machine():
    return render_template("addmachine.html")


@app.route("/insert_machine", methods=["POST"])
def insert_machine():
    machines = mongo.db.machines
    machines.insert_one(request.form.to_dict())
    return redirect(url_for("get_machines"))


@app.route('/edit_machine/<machine_id>')
def edit_machine(machine_id):
    the_machine = mongo.db.machines.find_one({"_id": ObjectId(machine_id)})
    return render_template('editmachinestatus.html', machine=the_machine)


@app.route("/update_machine/<machine_id>", methods=["GET", "POST"])
def update_machine(machine_id):
    machines = mongo.db.machines
    machines.update({"_id": ObjectId(machine_id)},
    {
         'machine_name': request.form.get('machine_name'),
         'is_in_production': request.form.get('is_in_production'),
         'comments': request.form.get('comments')

    })
    return redirect(url_for("get_machines"))


@app.route('/delet_machine/<machine_id>')
def delet_machine(machine_id):
    mongo.db.machines.remove({"_id": ObjectId(machine_id)})
    return redirect(url_for("get_machines"))


# -------Employee(CRUD)-------------
@app.route("/get_employees")
def get_employees():
    return render_template("employees.html",
                           employees=mongo.db.employees.find())


@app.route("/add_employee")
def add_employee():
    return render_template("addemployee.html")


@app.route("/insert_employee", methods=["POST"])
def insert_employee():
    employees = mongo.db.employees
    employees.insert_one(request.form.to_dict())
    return redirect(url_for("get_employees"))


@app.route('/edit_employee/<employee_id>')
def edit_employee(employee_id):
    the_employee = mongo.db.employees.find_one({"_id": ObjectId(employee_id)})
    return render_template('editemployee.html', employee=the_employee)


@app.route("/update_employee/<employee_id>", methods=["GET", "POST"])
def update_employee(employee_id):
    employees = mongo.db.employees
    employees.update({"_id": ObjectId(employee_id)},
    {
         'first_name': request.form.get('first_name'),
         'last_name': request.form.get('last_name'),
         'nick_name': request.form.get('nick_name')
    })
    return redirect(url_for("get_employees"))

@app.route('/delet_employee/<employee_id>')
def delet_employee(employee_id):
    mongo.db.employees.remove({"_id": ObjectId(employee_id)})
    return redirect(url_for("get_employees"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
