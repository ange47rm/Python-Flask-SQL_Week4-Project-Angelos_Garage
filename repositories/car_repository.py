from db.run_sql import run_sql

from models.car import Car
from models.manufacturer import Manufacturer

import repositories.manufacturer_repository as manufacturer_repository


def save (car):
    sql = 'INSERT INTO cars (manufacturer_id, manufacturer, model, engine_size, colour, mileage, year, purchase_cost, selling_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *'
    values = [car.manufacturer.id, car.manufacturer.name, car.model, car.engine_size, car.colour, car.mileage, car.year, car.purchase_cost, car.selling_price]

    results = run_sql (sql, values)
    print (results)
    car.id = results[0]['id']
    return car


def select_all ():
    cars = []

    sql = 'SELECT * FROM cars'
    results = run_sql (sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        car = Car (manufacturer, row['model'], row['engine_size'], row['colour'], row['mileage'], row['year'], row['purchase_cost'], row['selling_price'], row['id'])
        cars.append(car)
    return cars


def select (id):
    car = None

    sql = 'SELECT * FROM cars WHERE id = %s'
    value = [id]
    result = run_sql(sql, value)[0]

    if result is not None:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        car = Car (manufacturer, result['model'], result['engine_size'], result['colour'], result['mileage'], result['year'], result['purchase_cost'], result['selling_price'], result['id'])
    return car


def delete_all ():
    sql = 'DELETE FROM cars'
    run_sql (sql)


def delete(id):
    sql = "DELETE  FROM cars WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update (car):
    sql = 'UPDATE cars SET (manufacturer_id, model, engine_size, colour, mileage, year, purchase_cost, selling_price) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s'
    values = [car.manufacturer.id, car.model, car.engine_size, car.colour, car.mileage, car.year, car.purchase_cost, car.selling_price, car.id]
    
    print (values)
    run_sql (sql,values)


