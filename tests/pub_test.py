import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink = Drink("beer",10.00)
        
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_cash(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_list_of_drinks_has_drink(self):
        self.add_drink(self)
        self.assertEqual(1, len(self.pub.list_of_drinks))
    
