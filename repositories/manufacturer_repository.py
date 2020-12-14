from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.car import Car

def save (manufacturer):
    sql = 'INSERT INTO manufacturers (name, phone, email, website) VALUES (%s, %s, %s, %s) RETURNING *'
    values = [manufacturer.name, manufacturer.phone, manufacturer.email, manufacturer.website]

    results = run_sql (sql, values)
    print (results) ### added for demo purposes
    manufacturer.id = results[0]['id']
    return manufacturer


def select_all ():
    manufacturers = []

    sql = 'SELECT * FROM manufacturers'
    results = run_sql (sql)

    for row in results:
        manufacturer = Manufacturer (row['name'], row['phone'], row['email'], row['website'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers


def select (id):
    manufacturer = None

    sql = 'SELECT * FROM manufacturers WHERE id = %s'
    value = [id]

    result = run_sql (sql, value)[0]

    if result is not None:
        manufacturer = Manufacturer (result['name'], result['phone'], result['email'], result['website'], result['id'])
    return manufacturer


def delete_all ():
    sql = 'DELETE FROM manufacturers'
    run_sql(sql)

    
def update (manufacturer):
    sql = 'UPDATE manufacturers SET (name, phone, email, website) = (%s, %s, %s, %s) WHERE id = %s'
    values = [manufacturer.name, manufacturer.phone, manufacturer.email, manufacturer.website, manufacturer.id]
    run_sql (sql, values)

