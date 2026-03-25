# with keyword in file handling
# with automatically closes the file. No need to add file.close() method

# -> file = open("chapter-8/test3.txt", "r")
# -> data = file.read()

with open("chapter-8/test.txt", "r") as f:
    data = f.read()
    print(f"File data -> {data}")
    
# Reading file linebyline
with open("chapter-8/test2.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    data = f.read()
    print(f"File data -> {line1}")
    print(f"File data -> {line3}")
    print(f"File data -> {data}")
    
with open("chapter-8/test.txt", "r") as f:
    readlinemethod = f.readlines() # read lines and provides them in a list
    print(readlinemethod)