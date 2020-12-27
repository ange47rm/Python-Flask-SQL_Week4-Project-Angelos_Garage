from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.manufacturer import Manufacturer
from models.car import Car


import repositories.car_repository as car_repository
import repositories.manufacturer_repository as manufacturer_repository

car_blueprint = Blueprint ('car', __name__)

# CRUD: SELECT
# Return a list of all available cars/items.
@car_blueprint.route ('/cars')
def cars ():
    cars = car_repository.select_all()
    manufacturers = manufacturer_repository.select_all()
    return render_template ('cars/cars.html', page_title='CARS IN STOCK', cars=cars, all_manufacturers=manufacturers)

# CRUD: SELECT
# Return details for a single car/item.
@car_blueprint.route ('/cars/<id>')
def show_car (id):
    car = car_repository.select(id)
    return render_template ('cars/show.html', car=car)

# NEW (-> CRUD: CREATE)
# Return a form for creating a new car/item.
@car_blueprint.route ('/cars/create-new')
def new_car ():
    manufacturers = manufacturer_repository.select_all()
    return render_template ('cars/create-new.html', all_manufacturers=manufacturers)

# CRUD: CREATE
# Create a new car/item using details from the previous form. A Python Car object is created and saved in the SQL db.
# Finally it redirects the user to the '/cars', showing the newly created item.
@car_blueprint.route ('/cars', methods=['POST'])
def create_car ():
    manufacturer = manufacturer_repository.select(request.form['manufacturer_id'])
    model = request.form['model']
    engine_size = request.form['engine_size']
    colour = request.form['colour']
    mileage = request.form['mileage']
    year = request.form['year']
    purchase_cost = request.form['purchase_cost']
    selling_price = request.form['selling_price']
    car = Car (manufacturer, model, engine_size, colour, mileage, year, purchase_cost, selling_price)
    car_repository.save(car)
    return redirect('/cars')

# EDIT (-> CRUD: UPDATE)
# Returns a form for editing a car/item.
@car_blueprint.route ('/cars/<id>/edit')
def edit_car(id):
    car = car_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template ('cars/edit.html', car=car, page_title='EDIT DETAILS', all_manufacturers=manufacturers)

# CRUD: UPDATE
# Updates details of an existing car/item using the details from the previous form.
# The user is redirected to the '/cars' page, which shows the changes applied.
@car_blueprint.route ('/cars/<id>', methods=['POST'])
def update_car(id):
    manufacturer = manufacturer_repository.select(request.form['manufacturer_id'])
    model = request.form['model']
    engine_size = request.form['engine_size']
    colour = request.form['colour']
    mileage = request.form['mileage']
    year = request.form['year']
    purchase_cost = request.form['purchase_cost']
    selling_price = request.form['selling_price']
    car = Car (manufacturer, model, engine_size, colour, mileage, year, purchase_cost, selling_price, id)
    car_repository.update(car)
    return redirect ('/cars')

# CRUD: DELETE
# Deletes a car/item (using its ID to identify it)
@car_blueprint.route("/cars/<id>/delete", methods=['POST'])
def delete_car(id):
    car_repository.delete(id)
    return redirect('/cars')

# CRUD: SELECT
# Returns a list of all cars/item related to a manufacturer.
@car_blueprint.route ('/cars/filter-by-manufacturer/<manufacturer_id>')
def filter_by_manufacturer (manufacturer_id):
    cars_filtered = car_repository.select_cars_by_manufacturer(manufacturer_id)
    return render_template ('cars/cars-filter.html', cars=cars_filtered)