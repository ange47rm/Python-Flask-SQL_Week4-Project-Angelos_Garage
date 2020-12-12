import unittest

from models.car import Car
from models.manufacturer import Manufacturer



class TestCar (unittest.TestCase):

    def setUp (self):

        self.manufacturer_1 = Manufacturer ('Mazda', '0123 456 789', 'email@mazda.com', 'www.mazda.com')
        self.manufacturer_2 = Manufacturer ('Alfa Romeo', '0123 451 749', 'email@alfaromeo.com', 'www.alfaromeo.com')
        self.manufacturer_3 = Manufacturer ('Nissan', '0142 446 719', 'email@nissan.com', 'www.nissan.com')
        self.manufacturer_4 = Manufacturer ('Subaru', '0155 456 134', 'email@subaru.com', 'www.subaru.com')

        self.car_1 = Car (self.manufacturer_1.name, 'RX7', '1300cc', 'White', 54000, 1989, 9500, 12000)
        self.car_2 = Car (self.manufacturer_2.name, '1750 GT Veloce', '1800cc', 'Red', 75000, 1971, 34000, 45000)
        self.car_3 = Car (self.manufacturer_3.name, '240Z', '2400cc', 'Orange', 31000, 1970, 17500, 26000)
        self.car_4 = Car (self.manufacturer_4.name, 'Impreza', '2000cc', 'Blue', 130000, 1999, 6750, 9500)

    def test_car_has_manufacturer_name (self):
        self.assertEqual ('Mazda', self.car_1.manufacturer)

    def test_car_has_model (self):
        self.assertEqual ('1750 GT Veloce', self.car_2.model)

    def test_car_has_engine_size (self):
        self.assertEqual ('2400cc', self.car_3.engine_size)

    def test_car_has_colour (self):
        self.assertEqual ('Orange', self.car_3.colour)

    def test_car_has_mileage (self):
        self.assertEqual (130000, self.car_4.mileage)

    def test_car_has_year (self):
        self.assertEqual (1989, self.car_1.year)

    def test_car_has_purchase_cost (self):
        self.assertEqual (34000, self.car_2.purchase_cost)

    def test_car_has_selling_price (self):
        self.assertEqual (26000, self.car_3.selling_price)

    def test_car_has_id (self):
        self.assertEqual (None, self.car_2.id)