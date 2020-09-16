import unittest
from src.pub import Pub 

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Ox", 100.00)
        self.customer = Customer("Billy", 50.00)

    def test_pub_has_name(self):
        self.assertEqual("Ox", self.pub.name)

    def test_pub_has_cash(self):
        self.assertEqual(100.00, self.pub.cash)

    def test_customer_has_name(self):
        self.assertEqual("Billy", self.customer.name)
    
    def test_customer_has_cash(self):
        self.assertEqual(50.00, self.customer.cash)


