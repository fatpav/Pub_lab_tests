from src.drinks import Drinks 
from src.pub import Pub

class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def buy_drink(self, drink):
        self.wallet -= drink.price
        
        