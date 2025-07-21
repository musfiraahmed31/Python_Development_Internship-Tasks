counter = 0
print ("Initial Counter:",counter)

def change_counter():

    global counter  
    counter += 1    
    print("Counter is now:", counter)

change_counter()
change_counter()
change_counter()
