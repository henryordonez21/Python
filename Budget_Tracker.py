import os
from datetime import date

FILENAME = "transactions.txt"

def add_transaction():
    
    user_input = input("Press Enter for today's date or type your own (YYYY-MM-DD): ").strip()
    if user_input == "":
        final_date = str(date.today())
    else:
        final_date = user_input

    transaction_type = input("Type (income/expense): ").strip().lower()
    category = input("Category: ").strip()
    amount = input("Amount: ").strip()
    note = input("Note: ").strip()

    if transaction_type not in ["income", "expense"]:
        print("Invalid type. Must be 'income' or 'expense'")
        return
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Must be a number.")
        return
    
    with open(FILENAME, "a") as f:
        f.write(f"{final_date},{transaction_type},{category},{amount},{note}\n")

    print("Transaction Added!")

def view_transaction_by_type():
    transaction_type = input("Type (income/expense): ").strip().lower()
    if transaction_type not in ["income", "expense"]:
        print("Invalid Type")
        return

    if not os.path.exists(FILENAME):
        print("No transaction saved yet.\n")
        return
    
    found = False

    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",", 4)
            if len(data) != 5:
                continue
            stored_date, stored_type, category, amount, note = data

            if  stored_type == transaction_type:
                print(f"Date: {stored_date}")
                print(f"Type: {stored_type}")
                print(f"Category: {category}")
                print(f"Amount: {amount}")
                print(f"Note: {note}")
                print()
                found = True
        if not found:
            print("No entry found yet.\n")

def view_all():
    if not os.path.exists(FILENAME):
        print("No transactions saved yet.\n")
        return
    print("Saved transactions")
    print("-" * 30)
    found = False

    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",", 4)
            if len(data) != 5:
                continue
            stored_date, transaction_type, category, amount, note = data
            print(f"Date: {stored_date}")
            print(f"Type: {transaction_type}")
            print(f"Category: {category}")
            print(f"Amount: {amount}")
            print(f"Note: {note}")
            print()
            found = True
    if found:
        print("-" * 30)

    else:
        print("No transactions found.\n")

            
def show_summary():
    if not os.path.exists(FILENAME):
        print("No transactions saved yet.\n")
        return
    
    total_income = 0
    total_expense = 0

    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",", 4)
            if len(data) != 5:
                continue
            stored_date, stored_type, category, amount, note = data
            amount = float(amount)

            if stored_type == "income":
                total_income += amount
            elif stored_type == "expense":
                total_expense += amount

    balance = total_income - total_expense
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Balance: ${balance:.2f}")

def search_category():
    category = input("Enter category: \n").strip().lower()
    found = False

    if not os.path.exists(FILENAME):
        print("No transactions saved yet.\n")
        return
    
    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",", 4)
            if len(data) != 5:
                continue
            stored_date, transaction_type, stored_category, amount, note = data
            if stored_category.lower() == category:
                print(f"Date: {stored_date}")
                print(f"Type: {transaction_type}")
                print(f"Category: {stored_category}")
                print(f"Amount: {amount}")
                print(f"Note: {note}")
                print()
                found = True
        if not found:
            print("No category found yet.\n")
                
def main():
    while True:
        print("\nTransaction Tracker.")
        print("1. Add Transaction")
        print("2. View transactions by Type")
        print("3. Show Summary")
        print("4. Search Category")
        print("5. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transaction_by_type()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            search_category()
        elif choice == "5":
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
