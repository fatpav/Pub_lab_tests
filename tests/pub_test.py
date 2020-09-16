import unittest
from src.pub import Pub 
from src.customer import Customer
from src.drinks import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Ox", 100.00)
        self.customer_1 = Customer("Billy", 50.00, 18)
        self.customer_2 = Customer("Jimmy", 50.00, 16)
        self.drink_1 = Drink("Beer", 5.0)
        self.drink_2 = Drink("Wine", 7.5)
        self.drink_3 = Drink("Spirit", 3.5)
        self.drink_4 = Drink("Cocktail", 10.0)



    def test_pub_has_name(self):
        self.assertEqual("Ox", self.pub.name)

    def test_pub_has_cash(self):
        self.assertEqual(100.00, self.pub.cash)

    def test_customer_has_name(self):
        self.assertEqual("Billy", self.customer_1.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(50.00, self.customer_1.wallet)

    def test_drink_has_name(self):
        self.assertEqual("Beer", self.drink_1.name)

    def test_drink_has_price(self):
        self.assertEqual(5.00, self.drink_1.price)

    def test_customer_buy_drink(self):
        self.customer_1.buy_drink(self.drink_1)
        self.assertEqual(45, self.customer_1.wallet)

    def test_add_drink_to_menu(self):
        self.pub.add_drink_to_menu(self.drink_1)
        self.pub.add_drink_to_menu(self.drink_2)
        self.pub.add_drink_to_menu(self.drink_3)
        self.pub.add_drink_to_menu(self.drink_4)
        self.assertEqual(4, len(self.pub.menu))

    
    def test_add_to_cash(self):
        self.pub.sell_drink(self.drink_1)
        self.assertEqual(105.00, self.pub.cash)

    def test_customer_has_age(self):
        self.assertEqual(18, self.customer_1.age)
        self.assertEqual(16, self.customer_2.age)

    def test_age_check_adult(self):
        self.assertEqual(True, self.pub.age_check(self.customer_1))

    def test_age_check_adult(self):
        self.assertEqual(False, self.pub.age_check(self.customer_2))
    
    

    