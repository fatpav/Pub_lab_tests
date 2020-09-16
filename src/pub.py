class Pub:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.menu = []

    def add_drink_to_menu(self, drink):
        self.menu.append(drink)

    def sell_drink(self, drink):
        self.cash += drink.price

    def age_check(self, customer):
        if customer.age >= 18:
            return True
        
        return False
        
    



    
    