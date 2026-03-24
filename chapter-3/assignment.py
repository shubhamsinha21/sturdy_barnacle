# write a program to takes a sentence and prints:
# total characters (len())
# uppercase version of the string
# lowercase version of the string
# number of words in the string (split())

sentence = input("Enter a sentence: ")
print("Total characters:", len(sentence))
print("Uppercase version:", sentence.upper())
print("Lowercase version:", sentence.lower())
print("number of words in the string:", len(sentence.split()))
print("\n")

# write a program to take any word as input and print:
# first character of the word
# last character of the word
# middle character of the word
# length of the word    
# total no of characters in the word

word = input("Enter a word: ")
print("first charater of the word: ", word[0])
print("last character of the word:", word[-1])
print("middle character of the word:", word[len(word)//2])
print("length of the word:", len(word))
print("total no of characters in the word:", len(word))