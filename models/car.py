class Car ():
    def __init__(self, manufacturer, model, engine_size, colour, mileage, year, purchase_cost, selling_price, id = None):
        self.manufacturer = manufacturer
        self.model = model
        self.engine_size = engine_size
        self.colour = colour
        self.mileage = mileage
        self.year = year
        self.purchase_cost = purchase_cost
        self.selling_price = selling_price
        self.profit = int(self.selling_price) - int(self.purchase_cost)
        self.id = id
