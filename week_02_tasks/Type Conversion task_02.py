# Type Conversionntask_02
# Temperature Converter Program

print("=== Temperature Converter ===")

try:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F") #(Here .2f mean the 2 decimal values after point))

except ValueError:
    print("Invalid input! Please enter a numeric value for Celsius temperature.")

try:
    fahrenheit_input = float(input("\nEnter temperature in Fahrenheit: "))
    celsius_converted = (fahrenheit_input - 32) * 5/9
    print(f"{fahrenheit_input}°F is equal to {celsius_converted:.2f}°C")

except ValueError:
    print("Invalid input! Please enter a numeric value for Fahrenheit temperature.")
