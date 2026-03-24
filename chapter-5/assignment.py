# q1> dictionary that stores meanings of 3 words

dictionary = {'apple': 'is a fruit', 'almonds': 'is a dry fruit', 'ladyfinger': 'vegetable'}
print(dictionary)

# q2> create a set of numbers and show union and intersection with another set

set1 = {"apple", "mango", "banana"}
set2 = {"apple", "pineapple", "almonds"}

intersection = set1.intersection(set2)
print(intersection)

union = set1.union(set2)
print(union)

# q3> try to add 9 and 9.0 to a set and see results
set3 = {9, 10, 9.0} # not prints 9 and 9.0 both as it treats them as same value.
print(set3) 
