class CoffeeShop:
    
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.stock_drinks = {"Mocha": 15, "Latte": 25, "Hot Chocolate": 30, "Tea": 105}
        self.drinks_price = {"Mocha": 2.99, "Latte": 3.50, "Hot Chocolate": 3.10, "Tea": 2.50}
    

    def increase_till(self, amount):
        self.till += amount
    
    def check_age(self, age):
        if age >= 16:
            return "serve"
        return "don't serve"

    def check_energy_level(self, level):
        if level >= 100:
            return "serve"
        return "don't serve"

    def decrease_stock(self, drink):
        i = 0
        for i in self.stock_drinks:
            if i == drink:
                self.stock_drinks[drink] -= 1

    # Yep! Not very Pythonic.
    def get_stock_value(self):
        total_value = 0
        for i in self.stock_drinks:
            for j in self.drinks_price:
                if i == j:
                    total_value += self.stock_drinks[i] * self.drinks_price[j]
        return total_value



        
