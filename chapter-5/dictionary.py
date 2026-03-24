# dictionary methods

dict = {'name': 'Shubham', 'age': 25, 'city': 'Delhi'}
print(dict)
print(type(dict))
print(dict.keys()) # it will print the keys of the dictionary
print(dict.values()) # it will print the values of the dictionary
print(dict.items()) # it will print the key-value pairs of the dictionary

dict.pop("age") # it will remove the key-value pair with the key "age"
print(dict)

dict["title"] = "Python Developer" # it will add a new key-value pair to the dictionary
print(dict)

dict.update({"age": 25}) # it will update the value of the key "age" to 25
print(dict)    

dict.clear() # it will remove all the key-value pairs from the dictionary
print(dict)

# note - in dictionary , indexing and slicing is not possible as it is an unordered collection of key-value pairs.
