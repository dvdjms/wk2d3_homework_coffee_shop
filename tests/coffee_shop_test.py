import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer
class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self): # Arrange
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100.00)
        self.mocha = Drink("Mocha", 2.99, 3)
        self.latte = Drink("Latte", 3.50, 67)
        self.hot_chocolate = Drink("Hot Chocolate", 3.10, 70)
        self.tea = Drink("Tea", 2.50, 3)
        self.customer1 = Customer("John", 100.00, 15, 90)
        self.customer2 = Customer("Jane", 30.00, 18, 104)
        

    def test_coffee_shop_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)

    def test_increase_till(self):
        self.coffee_shop.increase_till(2.50) # Act
        self.assertEqual(102.50, self.coffee_shop.till) # Assert

    def test_check_for_drink(self):
        self.assertEqual("Mocha", self.mocha.name)
    
    def test_check_for_price(self):
        self.assertEqual(3.50, self.latte.price)

    def test_check_for_customer_name(self):
        self.assertEqual("John", self.customer1.name)

    def test_check_for_customer_wallet(self):
        self.assertEqual(100.00, self.customer1.wallet)
    
    def test_customer_buys_drink(self):
        self.customer1.decrease_wallet(-3.50)
        self.coffee_shop.increase_till(3.50)
        self.assertEqual(103.50, self.coffee_shop.till)
        self.assertEqual(96.50, self.customer1.wallet)

    def test_check_for_customer_age(self):
        # self.coffee_shop.check_age(self.customer.age)
        self.assertEqual("don't serve", self.coffee_shop.check_age(self.customer1.age))

    def test_check_for_customer_age(self):
        self.assertEqual("serve", self.coffee_shop.check_age(self.customer2.age))

    def test_get_energy_level(self):
        self.customer1.customer_energy("John", "Mocha")
        self.assertEqual(93, self.customer1.customer_energy(self.customer1.energy_level, self.mocha.caffeine_level))

    def test_customer_too_high(self):
        self.coffee_shop.check_energy_level(self.customer1.energy_level)
        self.assertEqual("don't serve", self.coffee_shop.check_energy_level(self.customer1.energy_level))

    def test_customer_too_high(self):
        self.coffee_shop.check_energy_level(self.customer2.energy_level)
        self.assertEqual("serve", self.coffee_shop.check_energy_level(self.customer2.energy_level))




    



# name
# customer
# wallet
# age

