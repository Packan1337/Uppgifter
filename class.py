class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return str(self.brand) + "\n" + str(self.model) + "\n" + (self.year)

car1 = str(Car("Mercedes", "E53 Coupé", "2022"))
car2 = str(Car("BMW", "M8 Grand Coupé", "2020"))

print(car1, car2, car2, car1, sep="\n\n")