# Monthly Savings Classification

try:
    Income = float(input("Enter your monthly income: "))
    Expenses = float(input("Enter your monthly expenses: "))

    Savings = Income - Expenses

    if Savings > 10000:
        Status = "Saving Well"

    elif 5000 <= Savings <= 9999:

        Status = "Average"

    elif Savings < 5000:

        Status = "Try to Save"

    else:
        Status = "Not Classified!"

    print("Your Savings are :", Savings)
    print("Status:", Status)

except ValueError:
    print("Error: Please enter valid numeric values.")
