import os
from datetime import datetime

FILENAME = "transactions.txt"

# Add income or expense
def add_transaction(transaction_type):
    while True:
        try:
            amount = float(input(f"Enter {transaction_type} amount: "))
            break
        except ValueError:
            print("Invalid number. Try again.")

    description = input("Enter description: ").strip()
    date = datetime.now().strftime("%Y-%m-%d")
    if transaction_type == "Expense":
        amount = -abs(amount)  # make sure expenses are negative

    with open(FILENAME, "a") as f:
        f.write(f"{amount},{transaction_type},{description},{date}\n")

    print(f"{transaction_type} saved!\n")

# View all transactions
def view_transactions():
    if not os.path.exists(FILENAME):
        print("No transactions found.\n")
        return

    print("\nAll Transactions:")
    print("-" * 40)
    with open(FILENAME, "r") as f:
        for line in f:
            amount, t_type, desc, date = line.strip().split(",", 3)
            print(f"{date} | {t_type:7} | ${float(amount):8.2f} | {desc}")
    print("-" * 40 + "\n")

# View current balance
def view_balance():
    if not os.path.exists(FILENAME):
        print("Balance: $0.00\n")
        return

    balance = 0
    with open(FILENAME, "r") as f:
        for line in f:
            amount = float(line.strip().split(",", 1)[0])
            balance += amount
    print(f"Current Balance: ${balance:.2f}\n")

# Main menu
while True:
    print("Personal Budget Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View All Transactions")
    print("5. Quit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_transaction("Income")
    elif choice == "2":
        add_transaction("Expense")
    elif choice == "3":
        view_balance()
    elif choice == "4":
        view_transactions()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.\n")