# SMART TEMPERATURE CONTROL SYSTEM

# take input in celsius and priny its equivalent in fahrenheit and kelvin.
# (use explicit type conversion and arithmetic operators)

# formula for fahrenheit, F = (celsius * 9/5) + 32
# formula for kelvin, K = celsius + 273.15

print("Enter the temp in celsius:")
celsius = float(input())
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print("The temperature in:" + "fahrenheit is " + str(fahrenheit) + " and in kelvin is " + str(kelvin))