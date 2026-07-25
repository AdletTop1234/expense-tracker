balance = 6500
expenses = [

]

def print_balance(balance):
    print("Your balance: ", end="")
    print(balance)

def add_expense(balance):
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
        return balance
    else:
        print("Not enough money")
        return balance

def show_all_expenses():
    n = 1
    total_expenses = 0

    if not expenses:
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

while True:
    print("1.Show Balance")
    print("2.Add Expense")
    print("3.Show All Expenses")
    print("4.Exit")
    print("Choose :")

    choice = input()

    if choice == "1":
        print_balance(balance)

    elif choice == "2":
        balance = add_expense(balance)

    elif choice == "3":
        show_all_expenses()

    elif choice == "4":
        print("GoodBye")
        break

    else:
        print("Incorrect Choice")