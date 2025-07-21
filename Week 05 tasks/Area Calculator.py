import math  

def calculate_area(radius):
    return math.pi * radius ** 2

r = float(input("Enter the radius of the circle: "))

area = calculate_area(r)
print(f"The area of the circle is: {area:.6f}")
