class CoffeeShop:
    
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount
    
    def drinks_count(self):
        print(len(self.drinks))

    def check_age(self, age):
        if age >= 16:
            return "serve"
        return "don't serve"

    def check_energy_level(self, level):
        if level >= 100:
            return "serve"
        return "don't serve"

    

