# Goal :
# print a countdown timer something "exciting" happens (like 'launching'... or 'hapy new year'..)
import time
count = int(input("Enter the counter number: "))

print("\nCountdown starts now: ")
for i in range(count, 0, -1):
    print(i)
    time.sleep(1)
    
print("Wohooo...you Won the match🔥")
    