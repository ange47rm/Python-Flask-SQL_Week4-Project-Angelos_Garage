from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.manufacturer import Manufacturer
from models.car import Car

import repositories.car_repository as car_repository
import repositories.manufacturer_repository as manufacturer_repository

manufacturer_blueprint = Blueprint ('manufacturer', __name__)

# CRUD: SELECT
# Return a list of all available manufacturers.
@manufacturer_blueprint.route ('/manufacturers')
def manufacturers ():
    manufacturers = manufacturer_repository.select_all()
    return render_template ('manufacturers/manufacturers.html', page_title='MANUFACTURERS', manufacturers=manufacturers)

# CRUD: SELECT
# Return details for a single manufacturer.
@manufacturer_blueprint.route ('/manufacturers/<id>')
def show_manufacturer (id):
    manufacturer = manufacturer_repository.select(id)
    return render_template ('manufacturers/show.html', manufacturer=manufacturer)

# NEW (-> CRUD: CREATE)
# Return a form for creating a new manufacturer.
@manufacturer_blueprint.route ('/manufacturers/create-new')
def new_manufacturer ():
    return render_template ('manufacturers/create-new.html')

# CRUD: CREATE
# Create a new manufacturer using details from the previous form. A Python Manufacturer object is created and saved in the SQL db.
# Finally it redirects the user to the '/manufacturer', showing the newly created item.
@manufacturer_blueprint.route ('/manufacturers', methods=['POST'])
def create_manufacturer():
    name = request.form ['name']
    phone = request.form ['phone']
    email = request.form ['email']
    website = request.form ['website']
    manufacturer = Manufacturer (name, phone, email, website)
    manufacturer_repository.save(manufacturer)
    return redirect ('/manufacturers')

# EDIT (-> CRUD: UPDATE)
# Returns a form for editing a manufacturer.
@manufacturer_blueprint.route ('/manufacturers/<id>/edit')
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template ('manufacturers/edit.html', page_title='EDIT DETAILS', manufacturer=manufacturer)

# CRUD: UPDATE
# Updates details of an existing manufacturer using the details from the previous form.
# The user is redirected to the '/manufacturers' page, which shows the changes applied.
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

# CRUD: DELETE
# Deletes a manufacturer (using its ID to identify it).
@manufacturer_blueprint.route("/manufacturers/<id>/delete", methods=['POST'])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')