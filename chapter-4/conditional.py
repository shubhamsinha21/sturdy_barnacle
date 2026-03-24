# conditional statements

marks = 85
if marks >=90:
    print("Grade A")
elif marks >=80:
    print("Grade B")
elif marks >=70:
    print("Grade C")
else:
    print("Grade D")
    
# take input and print +ve if no is > 0 and so on
num = float(input("Enter a number: "))
if num > 0:
    print("+")
elif num < 0:
    print("-")
else:
    print("0")