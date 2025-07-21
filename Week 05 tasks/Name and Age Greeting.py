def greet_user(name, age):

    return (f"Hello {name}, you are {age} years old.")

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

message = greet_user(user_name, user_age)
print(message)
