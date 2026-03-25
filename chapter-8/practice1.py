# q1> program to read text from a given file certificate.txt and find whether it contains the word live.
file = open("chapter-8/test.txt", "r")
data = file.read().lower()
print(f"\ndata is: {data}")
file.close()  # always close the file after opening

if "live" in data:
    print('\nYes, word "live" exists')
else:
    print("\nWord not exists")

# q2> open a file in write mode
file = open("chapter-8/test2.txt", "w") # replaces everytime we run the code
file.write("We are learning python...") 
file = open("chapter-8/test2.txt", "a") # append mode - adds more context
file.write("Helloee guys")

# q3> create a new file in x mode
file = open("chapter-8/test3.txt", "x") # replaces everytime we run the code
file.close()



