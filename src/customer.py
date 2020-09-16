from src.drinks import Drink 
from src.pub import Pub

class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.inebriation = 0

    def buy_drink(self, drink):
        self.wallet -= drink.price
        
        