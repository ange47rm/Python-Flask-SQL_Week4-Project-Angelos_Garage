from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.car import Car
from models.manufacturer import Manufacturer


import repositories.car_repository as car_repository
import repositories.manufacturer_repository as manufacturer_repository

garage_blueprint = Blueprint ('garage', __name__)

@garage_blueprint.route ('/')
def home ():
    return render_template ('index.html', page_title='Stock Management System')


# @garage_blueprint.route ('/cars')
# def cars ():
#     cars = car_repository.select_all()
#     return render_template ('cars/cars.html', page_title='Cars in stock', cars=cars)


# @garage_blueprint.route ('/cars/<id>')
# def show_car (id):
#     car = car_repository.select(id)
#     return render_template ('cars/show.html', car=car)


# @garage_blueprint.route ('/manufacturers')
# def manufacturers ():
#     manufacturers = manufacturer_repository.select_all()
#     return render_template ('manufacturers/manufacturers.html', page_title='Manufacturers', manufacturers=manufacturers)


# @garage_blueprint.route ('/manufacturers/<id>')
# def show_manufacturer (id):
#     manufacturer = manufacturer_repository.select(id)
#     return render_template ('manufacturers/show.html', manufacturer=manufacturer)


# @garage_blueprint.route ('/manufacturers/create-new')
# def new_manufacturer ():
#     return render_template ('manufacturers/create-new.html')


# @garage_blueprint.route ('/manufacturers', methods=['POST'])
# def create_manufacturer():
#     name = request.form ['name']
#     phone = request.form ['phone']
#     email = request.form ['email']
#     website = request.form ['website']
#     manufacturer = Manufacturer (name, phone, email, website)
#     manufacturer_repository.save(manufacturer)
#     return redirect ('/manufacturers')


# @garage_blueprint.route ('/cars/create-new')
# def new_car ():
#     manufacturers = manufacturer_repository.select_all()
#     return render_template ('cars/create-new.html', all_manufacturers=manufacturers)

    
# @garage_blueprint.route ('/cars', methods=['POST'])
# def create_car ():
#     manufacturer = manufacturer_repository.select(request.form['manufacturer_id'])
#     model = request.form['model']
#     engine_size = request.form['engine_size']
#     colour = request.form['colour']
#     mileage = request.form['mileage']
#     year = request.form['year']
#     purchase_cost = request.form['purchase_cost']
#     selling_price = request.form['selling_price']
#     car = Car (manufacturer, model, engine_size, colour, mileage, year, purchase_cost, selling_price)
#     car_repository.save(car)
#     return redirect('/cars')


# @garage_blueprint.route ('/manufacturers/<id>/edit')
# def edit_manufacturer(id):
#     manufacturer = manufacturer_repository.select(id)
#     return render_template ('manufacturers/edit.html', manufacturer=manufacturer)


# @garage_blueprint.route ('/manufacturers/<id>', methods=['POST'])
# def update_manufacturer (id):
#     name = request.form ['name']
#     phone = request.form ['phone']
#     email = request.form ['email']
#     website = request.form ['website']
#     manufacturer = Manufacturer (name, phone, email, website, id)
#     print (manufacturer.__dict__)
#     manufacturer_repository.update(manufacturer)
#     return redirect ('/manufacturers')


# @garage_blueprint.route ('/cars/<id>/edit')
# def edit_car(id):
#     car = car_repository.select(id)
#     # manufacturer = manufacturer_repository.select(id) - This was to hopefully get the current manufacturer to show for the product being edited without it defaulting to the top of the list.
#     manufacturers = manufacturer_repository.select_all()
#     return render_template ('cars/edit.html', car=car, all_manufacturers=manufacturers)


# @garage_blueprint.route ('/cars/<id>', methods=['POST'])
# def update_car(id):
#     manufacturer_id = manufacturer_repository.select(request.form['manufacturer_id'])
#     model = request.form['model']
#     engine_size = request.form['engine_size']
#     colour = request.form['colour']
#     mileage = request.form['mileage']
#     year = request.form['year']
#     purchase_cost = request.form['purchase_cost']
#     selling_price = request.form['selling_price']
#     car = Car (manufacturer_id, model, engine_size, colour, mileage, year, purchase_cost, selling_price, id)
#     car_repository.update(car)
#     return redirect ('/cars')


# @garage_blueprint.route("/cars/<id>/delete", methods=['POST'])
# def delete_car(id):
#     car_repository.delete(id)
#     return redirect('/cars')


# @garage_blueprint.route("/manufacturers/<id>/delete", methods=['POST'])
# def delete_manufacturer(id):
#     manufacturer_repository.delete(id)
#     return redirect('/manufacturers')