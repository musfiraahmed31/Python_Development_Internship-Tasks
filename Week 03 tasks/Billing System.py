# Task: Billing System with Discount

try:

    NumberOfProducts = int(input("Enter the number of products: "))
    TotalPrice = float(input("Enter the total price: "))
    Discount = 0

    if TotalPrice > 1000 and NumberOfProducts > 3:
        Discount = TotalPrice * 0.15

    elif TotalPrice > 500:
        Discount = TotalPrice * 0.10

    else:
        Discount = 0

    FinalBill = TotalPrice - Discount

    print("Total Price:", TotalPrice)
    print("Discount Applied:", Discount)
    print("Final Bill to Pay:", FinalBill)

except ValueError:
    print("Error: Please enter valid numeric values.")
