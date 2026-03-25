# return statement

def multiply(a, b):
    return a*b

print(multiply(10,20))

# q3> write a fuction square(num) that returns the sqaure of a number

def square(num):
    return num**2

print(square(5))

# q4> write a function that takes a string and returns the count of vowels and consonants.

def countVowelConsonants(userInput):
    
    vowels = "aeiouAEIOU"
    countVowels = 0
    countConsonants = 0
    
    for char in userInput:
       if char.isalpha(): # method to check only the alphabetical characters and not numeric one
           if char in vowels:
               countVowels+=1
           else:
               countConsonants+=1
    
    return countVowels, countConsonants

# function call
vowels, consonants = countVowelConsonants("hello, mr , how are you1234")
print(vowels, consonants)

# q5> function that retuns the uppercase version of string
def convert_to_upper(word):
    return word.upper()
print(convert_to_upper("shubham"))