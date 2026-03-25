# q1> function named welcome message() that prints the "Python PROGRAMMING !" three times

def welMesg(): # function defintion
    n = int(input("Enter the number: "))
    print("\nPYTHON PROGRAMMING !\n" * n)

welMesg() # function call

# q2> why are functions used in programming ?
# - to manage the work easily for repetitive tasks
# - to make code more readable
# - easier testing and debugging

# function calling before defining it
# tup()

# - name tup() is not defined

# q2> write a function show_age(name, age) that prints: "Shubham is 25 years old"

def show_age(name, age):
    print(f"Age of {name} is {age} years.")
    
show_age("shubham", 25)
