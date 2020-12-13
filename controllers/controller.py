from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.car import Car
from models.manufacturer import Manufacturer


import repositories.car_repository as car_repository
import repositories.manufacturer_repository as manufacturer_repository

garage_blueprint = Blueprint ('garage', __name__)

@garage_blueprint.route ('/home')
def home ():
    return render_template ('index.html', page_title='Stock Management System')


@garage_blueprint.route ('/cars')
def cars ():
    cars = car_repository.select_all()
    return render_template ('cars/cars.html', page_title='Cars in stock', cars=cars)


@garage_blueprint.route ('/cars/<id>')
def show_car (id):
    car = car_repository.select_id(id)
    return render_template ('cars/show.html', car=car)


@garage_blueprint.route ('/manufacturers')
def manufacturers ():
    manufacturers = manufacturer_repository.select_all()
    return render_template ('manufacturers/manufacturers.html', page_title='Manufacturers', manufacturers=manufacturers)

@garage_blueprint.route ('/manufacturers/<id>')
def show_manufacturer (id):
    manufacturer = manufacturer_repository.select(id)
    return render_template ('manufacturers/show.html', manufacturer=manufacturer)



@garage_blueprint.route ('/manage')
def manage ():
    return render_template ('manage.html', page_title='Manage Stock')

    