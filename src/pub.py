from src.drink import Drink
from src.customer import Customer

class Pub:
    def __init__(self, input_name, input_till):
        self.name = input_name
        self.till = input_till
        self.list_of_drinks = []

    def add_drink(self, drink):
        self.list_of_drinks.append(drink)

    
