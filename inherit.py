# INHERITENCE IN CLASSES

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.fuel_level = 50

    def drive(self):
        print("Car is driving")

    def fill_up(self):
        print("Fill up car with gasoline")
        self.fuel_level = 100


#ElectricCar is a subclass of Car Class
#Car class is base/parent class
class ElectricCar(Car):
    def __init__(self, make, model):
        # "super()" means parent/base class
        # make sure super is init called when using for subclass
        super().__init__(make, model)
        # add additional properties to the ElectricCar
        self.range = 500

    def perform_service(self):
        print("Perform a service...")
    
    #overriding the parent class function
    def fill_up(self):
        print("Charge the car")



# car = Car("Honda", "Accord")
# car.drive()
# car.fill_up()

# another_car = Car("Subaru", "Legacy")
# another_car.fill_up()

electric_car = ElectricCar("Tesla", "Model Y")
electric_car.drive()
electric_car.fill_up()
electric_car.perform_service()