from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.manufacturer import Manufacturer
from models.car import Car

import repositories.car_repository as car_repository
import repositories.manufacturer_repository as manufacturer_repository

manufacturer_blueprint = Blueprint ('manufacturer', __name__)

@manufacturer_blueprint.route ('/manufacturers')
def manufacturers ():
    manufacturers = manufacturer_repository.select_all()
    return render_template ('manufacturers/manufacturers.html', page_title='MANUFACTURERS', manufacturers=manufacturers)


@manufacturer_blueprint.route ('/manufacturers/<id>')
def show_manufacturer (id):
    manufacturer = manufacturer_repository.select(id)
    return render_template ('manufacturers/show.html', manufacturer=manufacturer)


@manufacturer_blueprint.route ('/manufacturers/create-new')
def new_manufacturer ():
    return render_template ('manufacturers/create-new.html')


@manufacturer_blueprint.route ('/manufacturers', methods=['POST'])
def create_manufacturer():
    name = request.form ['name']
    phone = request.form ['phone']
    email = request.form ['email']
    website = request.form ['website']
    manufacturer = Manufacturer (name, phone, email, website)
    manufacturer_repository.save(manufacturer)
    return redirect ('/manufacturers')


@manufacturer_blueprint.route ('/manufacturers/<id>/edit')
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template ('manufacturers/edit.html', page_title='EDIT DETAILS', manufacturer=manufacturer)


@manufacturer_blueprint.route ('/manufacturers/<id>', methods=['POST'])
def update_manufacturer (id):
    name = request.form ['name']
    phone = request.form ['phone']
    email = request.form ['email']
    website = request.form ['website']
    manufacturer = Manufacturer (name, phone, email, website, id)
    print (manufacturer.__dict__)
    manufacturer_repository.update(manufacturer)
    return redirect ('/manufacturers')


@manufacturer_blueprint.route("/manufacturers/<id>/delete", methods=['POST'])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')