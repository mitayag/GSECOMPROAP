class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start_engine(self):
        print(f"{self.brand} engine started.")

class Car(Vehicle):
    def honk(self):
        print("Car honks: Beep beep!")

car = Car("Toyota")
car.start_engine()
car.honk()
