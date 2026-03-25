# q1> print the no of lines present in test2.txt

with open("chapter-8/test2.txt", "r") as f:
    lines = f.readlines()
    print(len(lines))
  
# q2> write your name and add into file named intro.txt
with open("chapter-8/intro.txt", "w") as f:
    f.write("Shubham") 

