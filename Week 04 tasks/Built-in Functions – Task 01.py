UserInput = input("Enter any Python value: ")

print("\nYou entered:", UserInput)
print("Data type before execution:", type(UserInput))

try:
    print("\nExecuting your input using exec():")

    exec(UserInput)

except Exception as Error:
    
    print("An error occurred while executing:", Error)
