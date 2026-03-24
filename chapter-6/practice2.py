# q5> program to start pattern 
# *
# * *
# * * *
# * * * *
# * * * * *
 
n = 1
while (n<=5):
    print("* " * n)
    n+=1
    
print(f"Updated value of n: {n}")

# q6> program to print the multiplication of any number using while loop
# 3 x 1 = 3
# 3 x 2 = 6
# .....
# 3 x 10 = 30

table_of_num = int(input("Enter the number: "))
n=1
while n<=10:
    print(f"{table_of_num} x {n} : {table_of_num * n}")
    n+=1
    
print(n)

