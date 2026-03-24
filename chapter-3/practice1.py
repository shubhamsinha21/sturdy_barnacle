# questions on slicing
# Q1 . take input and print middle 3 characters and last 2 characters of the string
strin = input("Enter a string: ")

# lets say we take green

length = len(strin)
print("Length of the string: ", length)

middle_index = length / 2 # for green it will be 5/2 = 2.5
middle_index = int(middle_index) # it will convert 2.5 to 2 or 
# we can use "// operator to get the integer value directly"
# middle_index = length // 2 # it will give us the integer value directly

print("Middle character: ", middle_index)

middle_3_char = strin[middle_index-1 : middle_index+2] # it will print the middle 3 characters of the string
print("Middle 3 characters: ", middle_3_char)

last_2_char = strin[-2:]
print("Last 2 characters: ", last_2_char)



