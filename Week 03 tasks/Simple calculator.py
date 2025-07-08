# Simple Python Calculator

print("+++++++++++ CALCULATOR ++++++++++")

try:
    FirstNumber = float(input("Enter the first number: "))
    Operator = input("Enter an operator (+, -, *, /, %, //, **): ")
    SecondNumber = float(input("Enter the second number: "))

    if Operator == '+':
        Result = FirstNumber + SecondNumber
        print(f"Result: {FirstNumber} + {SecondNumber} = {Result}")

    elif Operator == '-':
        Result = FirstNumber - SecondNumber
        print(f"Result: {FirstNumber} - {SecondNumber} = {Result}")

    elif Operator == '*':
        Result = FirstNumber * SecondNumber
        print(f"Result: {FirstNumber} * {SecondNumber} = {Result}")

    elif Operator == '/':
        if SecondNumber == 0:
            print("Error: Cannot divide by zero")
        else:
            Result = FirstNumber / SecondNumber
            print(f"Result: {FirstNumber} / {SecondNumber} = {Result}")

    elif Operator == '%':
        if SecondNumber == 0:
            print("Error: Cannot use modulus with zero")
        else:
            Result = FirstNumber % SecondNumber
            print(f"Result: {FirstNumber} % {SecondNumber} = {Result}")

    elif Operator == '//':
        if SecondNumber == 0:
            print("Error: Cannot use floor division by zero")
        else:
            Result = FirstNumber // SecondNumber
            print(f"Result: {FirstNumber} // {SecondNumber} = {Result}")

    elif Operator == '**':
        Result = FirstNumber ** SecondNumber
        print(f"Result: {FirstNumber} ** {SecondNumber} = {Result}")

    else:
        print("Invalid operator entered")

except ValueError:
    print("Error: Please enter valid numbers")
