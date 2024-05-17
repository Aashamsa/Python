class vehicle:
    def __init__ (self,brand,model):
        self.brand = brand
        self.model = model
class car(vehicle):
    def move(self):
        print("Drive!")
class boat(vehicle):
    def move(self):
        print("Sail!")
class plane(vehicle):
    def move(self):
        print("Fly!")
car1 = car("Ford","Mustang")
boat1 = boat("Ibiza","Touring")
plane1 = plane("Boeing","212")
for x in car1,boat1,plane1:
    print(x.brand)
    print(x.model)
    x.move()