import json

data = {

}

with open("dictionary.json","r")as file:
    data = json.load(file)

balance = data["balance"]
expenses = data["expenses"]

def save_data(data,balance,expenses):
    data["balance"] = balance
    data["expenses"] = expenses

    with open("dictionary.json","w")as file:
        json.dump(data,file)

def print_balance(balance):
    print("Your balance: ", end="")
    print(balance)

def add_expense(balance):
    print("Enter category: ")
    category = input()
    print("Enter amount: ")

    try:
        amount = int(input())
        if balance >= amount:
            balance -= amount
            expense = {
                "category": category,
                "amount": amount
            }
            expenses.append(expense)
            save_data(data, balance, expenses)
            return balance
        else:
            print("Not enough money")
            return balance
    except ValueError:
        print("Incorrect input")
        return balance

def deposit_balance(balance):
    try:
        print("Enter money :")
        amount = int(input())
        balance += amount
        save_data(data, balance, expenses)
        return balance
    except ValueError:
        print("Incorrect Input")

        return balance

def show_all_expenses():
    n = 1
    total_expenses = 0

    if not expenses:
        print("No expenses yet.")
    else:
        print("Your expenses: ")
        for expense in expenses:
            print(f"{n}.{expense['category']} - {expense['amount']}")
            n += 1
            total_expenses += expense["amount"]
        print(f"Total expenses :{total_expenses}")

def delete_expense(balance):
    try:
        print("Enter index of expense")
        n = int(input())
        if 0 < n <= len(expenses):
            deleted_expense = expenses.pop(n-1)
            balance += deleted_expense['amount']
            save_data(data, balance, expenses)
            return balance
        else:
            print("Out of Range")
            return balance

    except ValueError:
        print("Incorrect Input")
        return balance

while True:
    print("1.Show Balance")
    print("2.Add Expense")
    print("3.Show All Expenses")
    print("4.Deposit balance")
    print("5.Delete expense")
    print("6.Exit")
    print("Choose :")

    choice = input()

    if choice == "1":
        print_balance(balance)

    elif choice == "2":
        balance = add_expense(balance)

    elif choice == "3":
        show_all_expenses()

    elif choice == "4":
        balance = deposit_balance(balance)

    elif choice == "5":
        balance = delete_expense(balance)

    elif choice == "6":
        print("GoodBye")
        break

    else:
        print("Incorrect Choice")