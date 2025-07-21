def is_even_or_odd(number):

    if number % 2 == 0:
        return "This is an Even number."
    
    else:
        return "This is an Odd number."

num = int(input("Enter a number: "))

print ((is_even_or_odd(num)))
