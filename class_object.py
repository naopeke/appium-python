class Car:
    def __init__(self, brand, model): #constructor
        self.brand = brand
        self.model = model

    def show(self): #method
        print(f"{self.brand} and {self.model}")
    

honda = Car("Honda", "Civic")
honda.show()

#Inheritance
class Fiat(Car):
    def __init__(self, brand, model, color, year):
        super().__init__(brand, model) #super calls the parent class(Car)
        self.color = color
        self.year = year
    
    def show(self):
        print(f"{self.brand}, {self.model}{self.color}{self.year}")

fiat1 = Fiat("fiat", "500", "white", "2025")
fiat1.show()

#encapsulation
class Bank:
    def __init__(self, account):
        self.__account = account #private (cannot access from outside of this class)

    def get_account(self): #getter
        return self.__account

bank = Bank(1234)
print(bank.get_account())