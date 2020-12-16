from flask import Flask, render_template
# from controllers.controller import garage_blueprint
from controllers.garage_controller import garage_blueprint
from controllers.cars_controller import car_blueprint
from controllers.manufacturers_controller import manufacturer_blueprint

app = Flask (__name__)

app.register_blueprint(garage_blueprint)
app.register_blueprint(manufacturer_blueprint)
app.register_blueprint(car_blueprint)


if __name__ == '__main__':
    app.run(debug=True)