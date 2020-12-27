from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.car import Car
from models.manufacturer import Manufacturer


import repositories.car_repository as car_repository
import repositories.manufacturer_repository as manufacturer_repository

garage_blueprint = Blueprint ('garage', __name__)

# Returns the home page
@garage_blueprint.route ('/')
def home ():
    return render_template ('index.html', page_title='STOCK MANAGEMENT SYSTEM')