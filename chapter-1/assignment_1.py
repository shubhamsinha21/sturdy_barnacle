# take diameter as input from user and calculate area of circle
# by default - input() is a string, so we need to convert it to float using float() function

print("Enter diameter of circle : ")
diameter = float(input()) # typecasting input (str) to float
radius = diameter / 2
area = 3.14 * radius**2
print("Radius of circle is : " + str(radius))
print("Area of circle is :" + str(area))