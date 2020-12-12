import pdb
from models.car import Car
from models.manufacturer import Manufacturer

import repositories.car_repository as car_repository
import repositories.manufacturer_repository as manufacturer_repository


manufacturer_repository.delete_all ()

manufacturer_1 = Manufacturer ('Mazda', '0123 456 789', 'email@mazda.com', 'www.mazda.com')
manufacturer_2 = Manufacturer ('Alfa Romeo', '0123 451 749', 'email@alfaromeo.com', 'www.alfaromeo.com')
manufacturer_3 = Manufacturer ('Nissan', '0142 446 719', 'email@nissan.com', 'www.nissan.com')
manufacturer_4 = Manufacturer ('Subaru', '0155 456 134', 'email@subaru.com', 'www.subaru.com')

manufacturers = [manufacturer_1, manufacturer_2, manufacturer_3, manufacturer_4]
for manufacturer in manufacturers:
    manufacturer_repository.save (manufacturer)

# 4 manufacturer Python objects have been created and put in a list.
# For each one of them, we run the repository save CRUD function, to run the CREATE sql command and add each one to the manufacturers DB table.

