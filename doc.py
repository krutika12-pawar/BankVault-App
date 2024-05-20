"""class Car:

    # Constructor method
    def __init__(self, color, model, year):
        # Instance attributes
        self.color = color      
        self.model = model
        self.year = year
        self.speed = 0
        #accessing attributes of the class using .notation
        #print(f"{self.color} {self.model} is now going.")

    #class method
    def accelerate(self, increase):
        self.speed +=increase
        print(f"{self.model} is now going {self.speed} mph.")
# Creating objects (instances) of the Car class
car1 = Car("Red", "Toyota", 2022)
car2 = Car("Black", "Honda", 2020)

car1.accelerate(100)"""


class Vehicle:
    #The Vehicle class has attributes make, model, 
    #and year, along with methods start() and stop()
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def start(self):
        print("Starting the vehicle.")
        
    def stop(self):
        print("Stopping the vehicle.")
        
class Car(Vehicle):
    #The Car class inherits from the Vehicle class and adds
    # a fuel_type attribute
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
    #The Car class overrides the start() method from the Vehicle 
    # class to print a different message that includes the fuel type    
    def start(self):
        print(f"Starting the {self.make} {self.model} with 
            {self.fuel_type} fuel.")
    #The Car class also has a new drive() method specific to cars.   
    def drive(self):
        print(f"Driving the {self.make} {self.model}.")

# Creating a Car object
car = Car("Honda", "Civic", 2022, "gasoline")
car.start()  # Output: Starting the Honda Civic with gasoline fuel.
car.drive()  # Output: Driving the Honda Civic.
car.stop()   # Output: Stopping the vehicle.
