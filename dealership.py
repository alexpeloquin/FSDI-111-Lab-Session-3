from car import Car
from menu import menu

import pickle

# Save the sale information
# when the item is removed from inventory push to sales
# save sales array
# add a menu option to see the history
# add the bottom of the history show total amount of sales

# List of cars in the system
sales = []
inventory = []
data_file = "inventory.dat"
sales_file = "sales.dat"
vehicle_shown = -1

def save_sales():
    writter = open(sales_file,"wb")
    pickle.dump(sales,writter)
    writter.close()
    print("Sale Saved!")

def save_data():
    writter = open(data_file,"wb")
    pickle.dump(inventory,writter) # save the array of cars
    writter.close()
    print("Data Saved!!")

def load_data():
    reader = open(data_file,"rb")
    temp = pickle.load(reader)
    for car in temp:
        inventory.append(car) # put the car in array
    print("Loaded from DB: " + str(len(inventory)))

def load_sales():
    reader = open(sales_file,"rb")
    temp = pickle.load(reader)
    for car in temp:
        sales.append(car) # put the car in array
    print("Sales from DB: " + str(len(inventory)))

def count_year():
    count = 0
    y = int(input("What year of car are you looking for? I can tell you how many we have in that year. "))
    for i in inventory:
        print(i.year)
        if i.year == y:
            count +=1
    print("We have "+str(count))

# Logic to ask the user for the car info
# Create a car object
# Add the car to a list
def create_new():
    print("The user wants to create X")
    try:
        make = input("What is the make? ")
        year = int(input("What is the year? "))
        cyls = int(input("How many cylinders? "))
        color = input("What is the color? ")
        price = float(input("What is the price? "))
        v = Car(make,year,cyls,color,price)
        inventory.append(v)
        save_data() #save the array
        input("Car Created. Press Enter to continue")
    except:
        # something crashed above
        print("*** Your data is not valid ****")

    
def print_list():
    global vehicle_shown # importing a global vehicle into the function
    vehicle_shown = -1 # -1 means no vehicle is being shown
    print('-' *16)
    print(" Inventory ")
    print('-' *16)
    count = 1
    #travel the array for each car, print its info
    for i in inventory:
        print(str(count) + " - " + str(i.year) + "  " + i.make)
        count +=1
    print('-' *16)

    try:
        index = input("View Deatils: ")
        # if index its not empty
        # parse index to int
        if index !="":
            n = int(index)
            n -= 1
            vehicle_shown = n # save the index of vehicle shown
            element = inventory[n]
            element.print_info()
    except:
        print(" ** Error, please trying again ** ")

def sell_vehicle():
    #show the condnesed list only year and make
    #the user choose one vehicle
    print_list()
    global vehicle_shown # import the gloabl vehilce
    print("vehicle index," + str(vehicle_shown) )
    if (vehicle_shown >=0):
        #ask for confirmation on the sale
        conf = input("Do you really want to sell this vehcile? [Y/N]: ")
        if(conf == "Y" or conf =="y"):
            #sell
            print("Congrats! the sale is final")
            theV = inventory[vehicle_shown]
            del inventory[vehicle_shown] # remove the item
            save_data()
            theV.start_engine() # start the engine and drive away
            sales.append(theV) #add the vehcile to the sales
            save_sales()
        elif (conf == "N" or conf =="n"):
            #no sell
            print("Too bad, maybe next time")
        else:
            print("Wrong option, plese try again and type Y or N")
    else:
        print("No vehicle is being shown to the client")
    #if yes, print message and remove from array


def show_sales():
    load_sales() #load the sales history
    print("-"*20)
    print(" SALES HISTORY ")
    total = 0.0
    for car in sales:
        print(" " + str(car.year) + " " +car.make+ " " + str(car.price))
        total +=car.price
    print("-"*20)
    print(" Grand Total: " + str(total))
    input("Press enter to continue")

# Start the system
load_data() # load inventory from DB
selection=""
while selection != "x":
    selection = menu()
    if(selection == "1"):
        create_new()
    elif(selection == "2"):
        print_list()
    elif(selection == "3"):
        count_year()
    elif(selection == "4"):
        sell_vehicle()
    elif(selection == "5"):
        show_sales()
    
