# q3> write a program to print all even numbers bet 1 and 50 using while loop

num = 1
while num<50:
    if num % 2 == 0:
        print(num)
    num+=1
    
# q4> print the sum of first n natural numbers
# for ex - if n=5, sum = 1 + 2 + 3 + 4 + 5

n = int(input("Enter the number: "))
sum = 0
while n>=1:
   sum = sum + n
   n = n-1
print(sum)

    