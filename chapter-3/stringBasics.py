# ways to declare a string
string1 = "This is a string"
string2 = 'This is also a string'
string3 = '''This is also a string'''

print(string1)
print(string2)
print(string3)

# length of a string
a = "Hello"
length = len(a)
print(length)

# indexing
str = "ABCDEFG" # 0 1 2 3 4 4 5 6 
print(str[0]) # we cant change the value of a string as it is immutable
print(str[4])

# slicing
stri = "Gulab jamun"
print(stri[0:5]) # it will print from index 0 to 4
print(stri[6:11]) # it will print from index 6 to 10
print(stri[:7]) # it will print from index 0 to 5
print(stri[:]) # it will print the whole string
print(stri[6:]) # it will print from index 5 to the end of the string

# negative indexing
strin = "Python"
print(strin[-1]) # it will print the last character of the string
print(strin[-5: -2]) # it will print the characters from index -5 to -2 #
print(strin[-2: -1]) # it will print the characters from index -2 to -1