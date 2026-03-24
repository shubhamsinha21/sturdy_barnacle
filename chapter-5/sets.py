# collection of unordered, unique items

lang = {"Python", "Java", "C++", "Python"}
print(lang) # it will print the unique items in the set
print(type(lang))

# we can have emptySet = set() to create an empty set

# dictionary methods
lang.add("JavaScript") # it will add the element "JavaScript" to the set
print(lang) 
lang.remove("C++") # it will remove the element "C++" from the set
print(lang)
lang.discard("C++") # it will remove the element "C++" from the set if it is present, otherwise it will do nothing
print(lang)
# lang.clear() # it will remove all the elements from the set
# print(lang)

lang.union({"Ruby", "Go"}) # it will return a new set that is the union of the two sets
print(lang.union({"Ruby", "Go"}))
lang.intersection({"Python", "Java"}) # it will return a new set that is the intersection of the two sets
print(lang.intersection({"Python", "Java"}))
lang.difference({"Python", "Java"}) # it will return a new set that is the difference of the two sets
print(lang.difference({"Python", "Java"}))  