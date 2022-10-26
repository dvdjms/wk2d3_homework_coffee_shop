class Customer:

    def __init__(self, name, wallet, age, energy_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy_level = energy_level


    def decrease_wallet(self, amount):
        self.wallet += amount
    
    def customer_energy_drink(self, customer, drink):
        energy = customer + drink
        return energy

    def customer_energy_food(self, customer, food):
        energy = customer - food
        return energy
