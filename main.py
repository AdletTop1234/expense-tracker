balance = 6500
expenses = [

]

while True:
    print("1.Show Balance")
    print("2.Add Expense")
    print("3.Show All Expenses")
    print("4.Exit")
    print("Choose :")

    choice = input()

    if choice == "1":
        print("Your balance: ", end = "")
        print(balance)

    elif choice == "2":
        print("Enter category: ")
        category = input()

        print("Enter amount: ")
        amount = int(input())
        if balance >= amount:
            balance -= amount
            expense = {
                "category": category,
                "amount": amount
            }
            expenses.append(expense)
        else:
            print("Not enough money")

    elif choice == "3":
        n = 1
        total_expenses = 0
        if expenses == []:
            print("No expenses yet.")
        else:
            print("Your expenses: ")
            for expense in expenses:
                print(f"{n}.")
                print("Category :", expense["category"])
                print("Amount :", expense["amount"])
                n += 1
                total_expenses += expense["amount"]
            print(f"Total expenses :{total_expenses}")

    elif choice == "4":
        print("GoodBye")
        break

    else:
        print("Incorrect Choice")