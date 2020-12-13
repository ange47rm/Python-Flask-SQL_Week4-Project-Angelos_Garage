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


@garage_blueprint.route ('/inventory')
def inventory ():
    manufacturers = manufacturer_repository.select_all()
    cars = car_repository.select_all()
    return render_template ('inventory.html', page_title='Inventory', cars=cars)

    