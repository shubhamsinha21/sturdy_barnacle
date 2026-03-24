# q7> print all even numbers bet 1 and 20

for i in range(0, 20, 2):
    print(i)
    
print("\n-----\n")
    
# square of each number from 1 to 10 
for i in range(1, 11):
    i= i ** 2
    print(i)
    
print("\n-----\n")
    
# q8> multiplication table of any number entered by the user
n = int(input("Enter the number: "))
for i in range(1, 11):
    print(f"\n{n} * {i} = {n*i}")