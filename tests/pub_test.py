import unittest
from src.pub import Pub 
from src.customer import Customer
from src.drink import Drinks

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Ox", 100.00)
        self.customer = Customer("Billy", 50.00)
        self.drink_1 = Drink("Beer", 5.0)
        self.drink_2 = Drink("Wine", 7.5)
        self.drink_3 = Drink("Spirit", 3.5)
        self.drink_4 = Drink("Cocktail", 10.0)



    def test_pub_has_name(self):
        self.assertEqual("Ox", self.pub.name)

    def test_pub_has_cash(self):
        self.assertEqual(100.00, self.pub.cash)

    def test_customer_has_name(self):
        self.assertEqual("Billy", self.customer.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(50.00, self.customer.wallet)

    def test_drink_has_name(self):
        self.assertEqual("Beer", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(5.00, self.drink.price)

    def test_customer_buy_drink(self):
        self.customer.buy_drink(self.drink)
        self.assertEqual(45, self.customer.wallet)

    def test_add_drink_to_menu(self):
        self.pub.add_drink_to_menu(self.drink)
        self.assertEqual(4, len(self.pub.menu))

    @unittest.skip("delete this line to run the test")
    def test_add_to_cash(self):
        self.customer.buy_drink(self.drink)
        self.assertEqual(105.00, self.pub.cash)

    