from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.manufacturer import Manufacturer
from models.car import Car


import repositories.car_repository as car_repository
import repositories.manufacturer_repository as manufacturer_repository

car_blueprint = Blueprint ('car', __name__)

@car_blueprint.route ('/cars')
def cars ():
    cars = car_repository.select_all()
    return render_template ('cars/cars.html', page_title='CARS IN STOCK', cars=cars)


@car_blueprint.route ('/cars/<id>')
def show_car (id):
    car = car_repository.select(id)
    return render_template ('cars/show.html', car=car)


@car_blueprint.route ('/cars/create-new')
def new_car ():
    manufacturers = manufacturer_repository.select_all()
    return render_template ('cars/create-new.html', all_manufacturers=manufacturers)

    
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


@car_blueprint.route ('/cars/<id>/edit')
def edit_car(id):
    car = car_repository.select(id)
    # manufacturer = manufacturer_repository.select(id) - This was to hopefully get the current manufacturer to show for the product being edited without it defaulting to the top of the list.
    manufacturers = manufacturer_repository.select_all()
    return render_template ('cars/edit.html', car=car, page_title='EDIT DETAILS', all_manufacturers=manufacturers)


@car_blueprint.route ('/cars/<id>', methods=['POST'])
def update_car(id):
    manufacturer_id = manufacturer_repository.select(request.form['manufacturer_id'])
    model = request.form['model']
    engine_size = request.form['engine_size']
    colour = request.form['colour']
    mileage = request.form['mileage']
    year = request.form['year']
    purchase_cost = request.form['purchase_cost']
    selling_price = request.form['selling_price']
    car = Car (manufacturer_id, model, engine_size, colour, mileage, year, purchase_cost, selling_price, id)
    car_repository.update(car)
    return redirect ('/cars')


@car_blueprint.route("/cars/<id>/delete", methods=['POST'])
def delete_car(id):
    car_repository.delete(id)
    return redirect('/cars')