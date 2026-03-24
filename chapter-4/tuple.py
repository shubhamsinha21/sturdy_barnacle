# tuples basics
# tuples are immutable, meaning they cannot be changed after they are created
# tuples are defined using parentheses ()
# tuples can contain any type of data, including other tuples
# tuples can be indexed and sliced like lists

tup = ("1₹", "2₹", "3₹", "4₹", "5₹", 10)
print(tup)
print(tup[0]) # it will print the first element of the tuple
print(tup[1:4]) # it will print from index 1 to 3

# empty tuple
empty_tup = ()
print(empty_tup)
print(type(empty_tup))

# single element tuple
single_tup = (1,) # we need to add a comma after the element to make it a tuple
print(type(single_tup))
print(single_tup)

print(tup.index("3₹")) # it will print the index of the element "3₹"