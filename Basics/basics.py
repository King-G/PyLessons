import typing


# class NAME_OF_A_CLASS (...):

#   My Global Vars

#   def __init__(self):
#        pass

#   def my_function(arguments):
#        pass

#   def my_function(something, another = "test"): (default assignment)
#        pass

class Engine(object):
    def __init__(self, version = "V6"):
        self.version = version

class Vehicle(object):
    def __init__(self, name: str, doors: int, wheels: int):
        self.wheels: int = wheels
        self.name: str = name
        self.doors: int = doors
        self.current_speed: int = 0
        self.engine = Engine()

    def Drive(self, acceleration):
        self.current_speed += acceleration

    def __str__(self, type = "Vehicle"):
        return "{0} (type: {1}) has {2} wheels and driving at {3} km/h \n".format(self.name,
                                                                                  type,
                                                                                  self.wheels,
                                                                                  self.current_speed)

# __ => Conventional coding for private functions/variables
class Car(Vehicle):
    # __init__ => initialize (making an instance (object) of car)
    # class became an object (initializing) and that object is referred to as 'self'
    def __init__(self, name: str, doors: int = 4, wheels: int = 4):
        super(Car, self).__init__(name, doors, wheels)
        self.air_co = False # True (On) False (off)

    def Drive(self):
        super(Car, self).Drive(acceleration=5)

    def __str__(self):
        return super(Car, self).__str__("Car")

class Motorcycle(Vehicle):
    def __init__(self, name: str, wheels: int = 3):
        super(Motorcycle, self).__init__(name, 0, wheels)
        self.engine = Engine("M6")

    def Drive(self):
        super(Motorcycle, self).Drive(acceleration=10)

    def __str__(self):
        return super(Motorcycle, self).__str__("Motorcycle")



#  CAR
#  -> Engine
#  -> Wheels (property -> variable)
#  -> Doors (something you have -> therefore a property)
#  -> Drives (something the car does -> function -> definition)
#  -> Heat/airco (seomthing the car does -> function -> def)

# def = Definition
# (other codes: sub (vb.net), function (javascript), void, method)

if __name__ == "__main__":
    my_first_car = Car("Mercedes")
    my_first_car.air_co = True
    print(my_first_car)

    my_first_motorcycle = Motorcycle("Honda")
    print(my_first_motorcycle)

    print(str(my_first_motorcycle))
    print("We are done")
