# lists in python

foods = ['pizza', 'burger', 'pasta', 'salad']
print(foods)
foods[0] = 'sushi' # we can change the value of a list as it is mutable
print(foods)

# list slicing
print(foods[0:2]) # it will print from index 0 to 1
print(foods[1:]) # it will print from index 1 to the end of the list
print(foods[:3]) # it will print from index 0 to 2
print(foods[:]) # it will print the whole list

print(max(foods)) # it will print the maximum value in the list
print(min(foods)) # it will print the minimum value in the list

# list methods
foods.append('ice cream') # it will add the element at the end of the list
print(foods)
foods.insert(1, 'fries') # it will add the element at the specified index
print(foods)
foods.remove('pasta') # it will remove the specified element from the list
print(foods)
foods.pop() # it will remove the last element from the list
print(foods)
foods.pop(1) # it will remove the element at the specified index
print(foods)
foods.sort() # it will sort the list in ascending order
print(foods)
foods.sort(reverse=True) # it will sort the list in descending order
print(foods)    