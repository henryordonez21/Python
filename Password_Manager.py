
import os

FILENAME ="passwords.txt"

def add_password():

    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    with open(FILENAME, "a") as f:
        f.write(f"{website},{username},{password}\n")

    print("Password saved!\n")

def view_password():
    website = input("Enter Website: ").strip()
    found = False
    
    if not os.path.exists(FILENAME):
        print("No passwords saved yet. \n")
        return

    with open(FILENAME, "r") as f:
        for line in f:
            parts = line.strip().split(",",2)

            if len(parts) != 3:
                continue

            stored_site, username, password = parts

            if stored_site == website:
                print("\nUsername", username)
                print("Password:", password)
                print()
                found = True

    if not found:
        print("Website not found.\n")

def view_all():
    if not os.path.exists(FILENAME):
        print("No passwords saved yet.\n")
        return
    
    print("\nSaved Passwords:")
    print("-" * 30)

    with open(FILENAME, "r") as f:
        for line in f:
            parts = line.strip().split(",", 2)

            if len(parts) != 3:
                continue
            website,username,password = parts
            print(f"Website: {website} | Username: {username}")
    
    print("-" * 30)

def delete_password():
    website = input("Enter website to delete: ").strip()
    
    if not os.path.exists(FILENAME):
        print("No passwords saved yet.\n")
        return
    
    lines = []
    found = False

    with open(FILENAME, "r") as f:
        for line in f:
            parts = line.strip().split(",", 2)
            
            if len(parts) != 3:
                continue
            
            stored_site, username, password = parts

            if stored_site != website:
                lines.append(line)
            else:
                found = True

    with open(FILENAME, "w") as f:
        f.writelines(lines)

    if found:
        print("Password deleted.\n")
    else:
        print("Password not found.\n")

while True:
    print("Password Manager")
    print("1. Add Password")
    print("2. View Password")
    print("3. View All")
    print("4. Delete Password")
    print("5. Quit")

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
        break
    else:
        print("Invalid option\n")






           

            
