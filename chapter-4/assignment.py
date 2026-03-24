# Q1> ask user for 3 fav movies and store them in a list and print the list

fav_movies = input("Enter your 3 favorite movies separated by commas: ")
# WE CAN TAKE THE INPUT AS A SINGLE STRING AND THEN SPLIT IT INTO A LIST USING THE SPLIT() METHOD

# OR, we can take it one by one and append it to the list
# or we can use for loop to take input and append it to the list

# method 1
movies_list = fav_movies.split(",") # it will split the string into a list based on
print("Your favorite movies are:", movies_list)

# Q2> create a tuple of marks (5 subjects) and print the tuple, highest and lowest marks
marks_tuple = (90, 91, 92, 93, 55)
print("Marks tuple: ", max(marks_tuple))
print("Marks tuple: ", min(marks_tuple))

