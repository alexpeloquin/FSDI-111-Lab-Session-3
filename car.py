# A class can contain:
# attributes, contructor and methods

class Car:
    make = ""
    year = 0
    cylinders = 0
    color = ""
    price = 0.0

    # Constructor - the intialization of class attributes
    def __init__(self,make,year,cyls,color,price):
        #print("I'm the constructor of Car")
        self.make = make
        self.year = year
        self.cylinders = cyls
        self.color = color
        self.price = price

    #Methods
    def start_engine(self):
        print("Engine has started! Vroom!")

    def stop_engine(self):
        print("Engine has stopped! NO vroom NO")
    
    def print_info(self):
        print("Car: ")
        print("Make: " + self.make)
        print("Year: " + str(self.year))
        print("Cylinders: " + str(self.cylinders))
        print("Color: " + self.color)
        print("Price: " + str(self.price))

