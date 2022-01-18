#import MAthplotlib and csv writer and reader
from matplotlib import pyplot as plt
from csv import writer, reader
import random

def get_data():
    """ get_psi collects: tire psi, gas milage, the temperature and if it is in Ferinhiet or Celcius. No peramitars """
    #open csv file to append
    with open("psi.csv","a", newline='') as psi:
        
        x = True
        while x == True:
            csv_writer = writer(psi)
            #collect data from the user: tire psi, gas milage, the temperature and if it is in Ferinhiet or Celcius 
            user_psi = float(input("What is the psi of your tires "))
            gas = float(input("what gas milage did you get? miles/galon "))
            temp = float(input("What is the temperature? "))
            c_f = input("Is that Ferinhiet or Celcius? f/c ")
            
            #if the user inputs a temperature in Celcius convert it to Ferinhiet
            if c_f == "c":
                temp =  temp * 9/5 + 32
           
            #saves data into a list
            row =[user_psi, gas, temp, c_f]
           
            #appends the list to the csv file
            csv_writer.writerow(row)
           
            #gives user chance to close the data entry and move on
            again = input("Would you like to continue? y/n ")
            if again.lower() == "y":
                x = True
                
            else:
                x = False
                

def get_X():
    """Makes a list of what the tire psi levels where and save in varible x"""
    #open csv file
    with open("psi.csv","r") as psi:
        csv_reader = reader(psi)
        #make a list to add to
        x = []
        #iterate through the file and save the file at index 0 on each row to tire
        for row in csv_reader:
           tire = row[0]
            #append the tire pressuer to the list x
           x.append(tire)
    return x

def get_y():
    """Makes a list of what the gas milage levels where and save in varible y"""

    with open("psi.csv","r") as psi:
        csv_reader = reader(psi)
        #make a list to add to
        y = []
        #iterater throught the file and save the gas milage into the list y
        for row in csv_reader:
           gas = row[1]
           y.append(gas)
    return y
def get_temp():
    #open csv file once agin
    with open("psi.csv","r") as psi:
        csv_reader = reader(psi)
        #make a list to store the temperatures 
        t = []
        #iterate through the file and save the temperater levels into the list t
        for row in csv_reader:
            temp = float(row[2])
            t.append(float(temp))

    return t
    
def graph(x,y,t):
    """(tire_pressure, gas_milage, temp_F) needs a list"""
   
    #this plots each dot on graph, sets the color of the outline and color bar
    plt.scatter(x, y, c= t, cmap='RdBu_r', edgecolor = 'black', linewidth=1, alpha=.8)
    #labels the x_axis
    plt.xlabel("Tire Pressure (psi)")
    #sets a scale so outlires do not effect data
    plt.xscale("log")
    #labels the y_axis
    plt.ylabel("Miles/Gallon")
    #sets a scale so outlires do not effect data
    plt.yscale("log")
    #sets the color bar on the right side of the graph off of c="" in plt.scater
    cbar = plt.colorbar()
    #label the color bar on the right
    cbar.set_label('Temperature in F')
    #show the graph 
    plt.show()

def pop_psi():
    """Populates psi.csv with random values"""
    #open psi flie
    with open("psi.csv","a", newline='') as psi:
        csv_writer = writer(psi)

        for _ in range(1,100):
            user_psi = random.randint(60,100)
            gas = random.randint(5,33)
            temp = random.randint(-10,100)
            c_f = "f"
            row =[user_psi, gas, temp, c_f]
            #appends the list to the csv file
            csv_writer.writerow(row)


def main():
    # this just makes random points to graph just for testing
    #pop_psi() 

    #this asks the user for the data
    get_data()
    #stores the psi in the variable x
    x = get_X()
    #stores the gas milage data in a varible y
    y = get_y()
    #saves what the temerature was in t
    t = get_temp()
    #finaly graphs it all using matplot lib
    graph(x,y,t)

if __name__ == '__main__':
    main()

   



