# program to take a sentecnce as input
# converts it to lowercase
# replaces all spaces " " with hyphen "-"
# prints the modified string

print("Provide me the sentence:")
sentence = input()
modified_sentecnce = sentence.lower().replace(" ", "-")
print(modified_sentecnce)