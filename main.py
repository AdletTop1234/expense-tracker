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
        expense = {
            "category": category,
            "amount": amount
        }
        expenses.append(expense)
        balance = balance - amount

    elif choice == "3":
        print("Your expenses: ", end = "")
        for n in expenses:
            print(n)

    elif choice == "4":
        print("GoodBye")
        break

    else:
        print("Incorrect Choice")