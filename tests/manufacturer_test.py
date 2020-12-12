import unittest

from models.manufacturer import Manufacturer

class TestManufacturer (unittest.TestCase):

    def setUp (self):

        self.manufacturer_1 = Manufacturer ('Mazda', '0123 456 789', 'email@mazda.com', 'www.mazda.com')
        self.manufacturer_2 = Manufacturer ('Alfa Romeo', '0123 451 749', 'email@alfaromeo.com', 'www.alfaromeo.com')
        self.manufacturer_3 = Manufacturer ('Nissan', '0142 446 719', 'email@nissan.com', 'www.nissan.com')
        self.manufacturer_4 = Manufacturer ('Subaru', '0155 456 134', 'email@subaru.com', 'www.subaru.com')

    def test_manufacturer_has_name (self):
        self.assertEqual ('Mazda', self.manufacturer_1.name)

    def test_manufacturer_has_phone_no (self):
        self.assertEqual ('0123 451 749', self.manufacturer_2.phone)

    def test_manufacturer_has_email (self):
        self.assertEqual ('email@nissan.com', self.manufacturer_3.email)

    def test_manufacturer_has_website (self):
        self.assertEqual ('www.subaru.com', self.manufacturer_4.website)
