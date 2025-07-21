def square_numbers(numbers):

    return [num ** 2 for num in numbers]

input_list = input("Enter numbers: ")
number_list = [int(i) for i in input_list.split()]

squared_list = square_numbers(number_list)

print("Squared numbers:", squared_list)


