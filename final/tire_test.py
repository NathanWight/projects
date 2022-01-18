from csv import writer, reader

def test_writer():
    # this is how I tested the data input to make sure it placed it correctly in the csv file
    with open("test_psi.csv","w", newline='') as psi:
        
     
        csv_writer = writer(psi)
        #collect data from the user: tire psi, gas milage, the temperature and if it is in Ferinhiet or Celcius 
        user_psi = float(input("What is the psi of your tires "))
        
        #saves data into a list
        row =[user_psi]
           
        #appends the list to the csv file
        csv_writer.writerow(row)

        
    with open("test_psi.csv","r", newline='') as psi:
        #time to test if the data was stored properly 
        csv_reader = reader(psi)
        for line in csv_reader:
            test_user_psi = line[0]
    if user_psi == float(test_user_psi):
        print("it worked")
    else:
        print("something went wrong")


test_writer()