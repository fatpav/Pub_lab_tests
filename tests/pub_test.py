import unittest
from src.pub import Pub 
from src.customer import Customer
from src.drinks import Drinks

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Ox", 100.00)
        self.customer = Customer("Billy", 50.00)
        self.drink = Drinks("Beer", 5.00)

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