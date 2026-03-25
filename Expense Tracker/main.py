# Expense tracker project

expenses = [] # empty list with dictionaries

print("WELCOME TO EXPENSE TRACKER ✅")

while True:
    print("=======MENU=======")
    print("1. Add Expense")
    print("2. View all expenses")
    print("3. View total spending")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))

# add expenses    
    if choice == 1:
        date = input("When did the item bought ?: ")
        category = input("What is the category of item (books, clothes, etc): ")
        description = input("Write the description: ")
        amount = float(input("Enter the amount: "))
        
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        
        expenses.append(expense)
        print(f"\nDONE 👍🏻 Expense is added successfully.\n{expenses}\n")

# view all expenses
    elif choice == 2:
        if (len(expenses) == 0):
            print("No Expenses Added 🙂")
        else:
            print("These are your expenses 👉🏻")
            count = 1
            for i in expenses:
                print(f"{count} -> {i["date"]}, {i["category"]}, {i["description"]}, {i["amount"]}")
                count+=1

# View total spending
    elif choice == 3:
        total = 0
        for i in expenses:
            total = total + i["amount"]

        print("\n total expenditure: ", total)
            
# EXIT
    elif choice == 4:
        print("Thanks for using this 👉🏻  EXIT....")
        break
    
    else:
        print("Invalid choice. Try again !!")
