
print("=== Welcome to the Quick Survey ===\n")

name = input("1. What is your name? ")
fav_food = input("2. What is your favorite food? ")
birth_year = input("3. What year were you born? ")
fav_number = input("4. What is your favorite number? ")
fav_language = input("5. What is your favorite programming language? ")

print("\n=== Survey Summary ===\n")
print(f"Hello {name}, it's great to know about you!")
print(f"You love eating {fav_food}.")
print(f"You were born in {birth_year}, which makes you {2025 - int(birth_year)} years old (if it's 2025).")
print(f"Your favorite number is {fav_number}.")
print(f"And your favorite programming language is {fav_language}.")
print("\nThank you for participating in the survey!")
