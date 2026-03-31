import os
from datetime import datetime

FILENAME = "transactions.txt"

def add_transaction():

    date = input("Date: ").strip()
    try:
        date_obj =  datetime.strptime(date, "%Y-%m-%d")
        date = date_obj.strftime("%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD")
        return

    transaction_type = input("Income/Expense: ").strip().lower()
    category = input("Category: ").strip()
    amount = input("Amount: ").strip()
    note = input("Note: ").strip()

    if transaction_type not in ["income", "expense"]:
         print("Invalid choice. Must be income or expense")
         return
          
    try:
        amount = float(amount)
    except ValueError:
        print("Error: Invalid Input. Enter a valid number")
        return

    with open(FILENAME, "a") as f:
        f.write(f"{date},{transaction_type},{category},{amount},{note}\n")

    print("Transaction Added!")
            
def view_all():
    if not os.path.exists(FILENAME):
        print("No transactions added yet.\n")
        return
    found = False
    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",", 4)

            if len(data) != 5:
                continue

            date, transaction_type, category, amount, note = data
            print(f"Date: {date}")
            print(f"Type: {transaction_type}")
            print(f"Category: {category}")
            print(f"Amount: {amount}")
            print(f"Note: {note}")
            print()
            found = True
    if not found:
        print("Nothing found yet.\n")

def view_by_type():
    transaction_type = input("Would you like to view income or expense?").strip().lower()

    if not os.path.exists(FILENAME):
        print("No transactions added yet.\n")
        return

    if transaction_type not in ["income", "expense"]:
        print("Invalid choice. Must be income or expense")
        return
    
    found = False
    print("-" * 30)

    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",", 4)

            if len(data) != 5:
                continue

            date, stored_type, category, amount, note = data

            if stored_type == transaction_type:
                print(f"Date: {date}")
                print(f"Type: {stored_type}")
                print(f"Category: {category}")
                print(f"Amount: {amount}")
                print(f"Note: {note}")
                print()
                found = True
    if not found:
        print("Nothing found yet.\n")

    print("-" * 30)

def totals_by_category():
    if not os.path.exists(FILENAME):
        print("No transactions added yet.\n")
        return
    
    totals_category = {}
    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",", 4)

            if len(data) != 5:
                continue

            date, transaction_type, category, amount, note =  data

            try: 
                amount = float(amount)
            except ValueError:
                print("Error: Invalid Input. Enter a valid number")
                continue
            
            if transaction_type == "expense":
                amount = -amount

            if category in totals_category:
                totals_category[category] += amount
            else:
                totals_category[category] = amount

    for category, total in totals_category.items():
        if total < 0:
            print(f"{category} -${abs(total):.2f}")
        else:
            print(f"{category}: ${total:.2f}")


def monthly_summary():
    choice_date = input("Month: ").strip()
    try:
        date_obj = datetime.strptime(choice_date,"%Y-%m")
        
    except ValueError:
        print("Invalid date format. Enter it as YYYY-MM")
        return
    
    total_income = 0
    total_expense = 0
    found = False

    if not os.path.exists(FILENAME):
        print("No transactions added yet.\n")
        return
    
    print(f"Monthly Summary for {choice_date}")
    print("-" * 30)
    
    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",", 4)

            if len(data) != 5:
                continue

            stored_date, transaction_type, category, amount, note = data

            if stored_date.startswith(choice_date):
                continue
            
            found = True

            try:
                amount = float(amount)
            except ValueError:
                print("Error: Invalid Input. Enter a valid number")
                continue

            if transaction_type == "income":
                total_income += amount
            elif transaction_type == "expense":
                total_expense += amount
    if not found:
        print("No transactions found for this month.\n")
    
    else:

        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expense: ${total_expense:.2f}")
        print(f"Balance: ${total_income - total_expense:.2f}")
        print("-"* 30)

def show_summary():
    total_income = 0
    total_expense = 0

    if not os.path.exists(FILENAME):
        print("No transactions added yet. \n")
        return

    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",", 4)

            if len(data) != 5:
                continue

            date, stored_type, category, amount, note = data

            try:
                amount = float(amount)
            except ValueError:
                print("Error: Invalid Input. Enter a valid number")
                continue

            if stored_type == "income":
                total_income += amount

            elif stored_type == "expense":
                total_expense += amount
    
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expense: ${total_expense:.2f}")
    print(f"Balance: ${total_income - total_expense:.2f}")

def main():
    while True:

        print("Budget Tracker")
        print("\n1. Add Transaction")
        print("2. View all transactions")
        print("3. View by Type")
        print("4. Show summary")
        print("5. Totals by category")
        print("6. Monthly Summary")
        print("7. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_all()
        elif choice  == "3":
            view_by_type()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            totals_by_category()
        elif choice == "6":
            monthly_summary()
        elif choice == "7":
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()    
