# Datatypes_task 01

name = "Musfira Ahmed"               
age = 18                     
height = 5.9                 
is_student = True            
complex_num = 4 + 3j         

print("Value and datatypes before conversion")

print(f"name: {name} : {type(name)}")
print(f"age: {age} : {type(age)}")
print(f"height: {height} : {type(height)}")
print(f"is_student: {is_student} : {type(is_student)}")
print(f"complex_num: {complex_num} : {type(complex_num)}")

print("\nAfter Conversion:\n")

# String to Integer (in case if string is not a number then conversion from string to integer is failed)
# Handling conversion errors

try:
    name_to_int = int(name)
    print(f"Converted 'name' to int: {name_to_int} : {type(name_to_int)}")

except ValueError:
    print("Cannot convert 'name' (string) to int (integer)")

# Integer to Float

age_to_float = float(age)
print(f"Converted 'age' to float: {age_to_float} : {type(age_to_float)}")

# Float to String

height_to_string = str(height)
print(f"Converted 'height' to string: {height_to_string} : {type(height_to_string)}")

# Boolean to Integer
student_to_int = int(is_student)
print(f"Converted 'is_student' to int: {student_to_int} : {type(student_to_int)}")

# Complex to String
complex_to_string = str(complex_num)
print(f"Converted 'complex_num' to string: {complex_to_string} : {type(complex_to_string)}")

# Convert complex to float (will fail)
# Only the real part conversion is possible in python
try:
    complex_to_float = float(complex_num)
    print(f"Converted 'complex_num' to float: {complex_to_float} : {type(complex_to_float)}")

except TypeError:
    print("Cannot convert complex number directly to float.")
