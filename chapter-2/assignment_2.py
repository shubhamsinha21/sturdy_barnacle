# program that takes total bill amount and number of friends as input.
# calculate how much each person will pay.
# also print the data tye of each variable used in the program.

print("Enter the total bill amount:")
bill_amount = float(input())
print("Enter the number of friends:")
num_friends = int(input())

each_person_pays = bill_amount / num_friends
print("Each person will pay: " + str(each_person_pays))
print("Data type of bill_amount is: ", type(bill_amount))
print("Data type of num_friends is: ", type(num_friends))
print("Data type of each_person_pays is: ", type(each_person_pays))
