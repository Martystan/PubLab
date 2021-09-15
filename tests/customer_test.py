import unittest
from src.customer import Customer
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jim", 45)
    
    def test_customer_name(self):
        self.assertEqual("Jim", self.customer.name)

    def test_customer_funds(self):
        self.assertEqual(45, self.customer.wallet)

    # def test_remove_drink_from(self):
    #     self.remove_drink_from(self, self.pub.list_of_drinks, "beer")
    #     self.assertEqual(0, len(self.pub.list_of_drinks))