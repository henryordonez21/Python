
import os

FILENAME = "passwords.txt"

def add_password():
    website =  input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    with open(FILENAME, "r") as f:
        found = False
        for line in f:
            parts = line.strip().split(",",2)
            file_website, file_username, _ = parts
            if file_website.lower() == website.lower() and file_username.lower() == username.lower():
                found = True
                print("Duplicate found! Password not saved.")
                return 

    with open(FILENAME, "a") as f:
        f.write(f"{website},{username},{password}\n")

    print("Password Saved!")

def view_password():
    website = input("Enter website: ").strip()
    found = False

    if not os.path.exists(FILENAME):
        print("No passwords saved yet.\n")
        return
    
    with open(FILENAME,"r") as f:
        for line in f:
            parts = line.strip().split(",", 2)

            if len(parts) != 3:
                continue

            stored_site, username, password = parts

            if stored_site.lower() == website.lower():
                print("Username", username)
                print("Password", password)
                print()
                found = True

        if not found:
            print("No passwords found.\n")

def view_all():
    if not os.path.exists(FILENAME):
        print("No passwords saved yet.\n")
        return
    
    print("Saved Passwords")
    print("-" * 30)
    with open(FILENAME,"r") as f:
        for line in f:
            parts = line.strip().split(",", 2)

            if len(parts) != 3:
                continue
            website, username, password = parts
            print(f"Website: {website} | Username: {username}")

    print("-" * 30)

def delete_password():
    website = input("Enter website to delete: \n").strip()

    if not os.path.exists(FILENAME):
        print("No passwords saved yet. \n")
        return
    
    lines = []
    found = False

    with open(FILENAME, "r") as f:
        for line in f:
            parts = line.strip().split(",", 2)

            if len(parts) != 3:
                continue
            stored_site, username, password = parts

            if stored_site.lower() != website.lower():
                lines.append(line)
            else:
                found = True
                
    with open(FILENAME, "w") as f:
        f.writelines(lines)

    if found:
        print("Password deleted.\n")
    else:
        print("Password not found.\n")

def search_password():
    website = input("Enter website to find passwords for:").strip()
    found = False
    if not os.path.exists(FILENAME):
        print("No passwords saved yet.\n")
        return

    with open(FILENAME, "r") as f:
        for line in f:
            parts = line.strip().split(",", 2)

            if len(parts) != 3:
                continue
            stored_site, username, password = parts

            if stored_site.lower() == website.lower():
                print(f"Username:", username)
                print(f"Password:", password)
                print()
                found = True

    if not found:
            print("No password found for this website.\n")

while True:
    print("Password Manager")
    print("1. Add Password")
    print("2. View Password")
    print("3. View All Passwords")
    print("4. Delete Password")
    print("5. Search Passwords")
    print("6. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_password()
    elif choice == "2":
        view_password()
    elif choice == "3":
        view_all()
    elif choice == "4":
        delete_password()
    elif choice == "5":
        search_password()
    elif choice == "6":
        break
    else:
        print("Not a valid input")




           

            
