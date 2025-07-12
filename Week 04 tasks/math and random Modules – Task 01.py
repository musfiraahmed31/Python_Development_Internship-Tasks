import math # math library imported

Radius = float(input("Enter the radius of the circle: ")) # take input from user

Area = math.pi * Radius ** 2
Circumference = 2 * math.pi * Radius
SqrtArea = math.sqrt(Area)

# print the results

print(f"Area of Circle: {Area:.5f}")
print(f"Circumference: {Circumference:.5f}")
print(f"Square Root of Area: {SqrtArea:.5f}")

