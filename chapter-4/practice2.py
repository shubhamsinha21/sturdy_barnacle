# create a tuple of fav 5 fruits and print the tuple
# total no of fruits in the tuple
# index of one selected fruit

fruits = ("apple", "banana", "orange", "grape", "mango")
print("Fruits tuple: ", fruits)

total_fruits = len(fruits)
print("Total number of fruits: ", total_fruits)

selected_fruit = input("Enter the name of a fruit to find its index: ")
if selected_fruit in fruits:
    index = fruits.index(selected_fruit)
    print(f"The index of {selected_fruit} is {index}")
else:
    print(f"{selected_fruit} is not in the fruits tuple")