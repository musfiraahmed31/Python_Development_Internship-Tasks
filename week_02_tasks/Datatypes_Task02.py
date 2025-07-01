# Data Type Tester Program

user_input = input("Enter any value: ")

print(f"\nPython sees this input as type: {type(user_input)}")

if user_input.lower() == "true" or user_input.lower() == "false":
    print("This is likely a Boolean value.")

try:
    int_value = int(user_input)
    print("You enter an integer.")
    print (type(int_value))


except ValueError:
    
    try:
        float_value = float(user_input)
        print("You enter a float.")
        print (type(float_value))


    except ValueError:

        print("You enter a string.")

