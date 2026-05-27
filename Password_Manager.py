import os

FILENAME = "passwords.txt"

def parse_line(line):
    parts = line.strip().split(",", 2)
    if len(parts) != 3:
        return None
    return parts    

def add_password():
    if not os.path.exists(FILENAME):
        open(FILENAME, "w").close()

    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    with open(FILENAME, "r") as f:
        found = False

        for line in f:
            data = parse_line(line)
            if not data:
                continue

            stored_site, stored_username, _ = data

            if stored_site.lower() == website.lower() and stored_username.lower() == username.lower():
                found = True
                print("Duplicate found! Password not saved.")
                return

    with open(FILENAME, "a") as f:
        f.write(f"{website},{username},{password}\n")
        
    print("Password has been saved!")

def view_password():
    website = input("Enter website: ").strip()
    found = False

    if not os.path.exists(FILENAME):
        print("No passwords saved yet.\n")
        return
    
    with open(FILENAME, "r") as f:

        for line in f:
            data = parse_line(line)
            if not data:
                continue

            stored_site, stored_username, stored_password = data

            if stored_site.lower() == website.lower():
                print(f"Username: {stored_username}")
                print(f"Password: {stored_password}")
                print()
                found = True

        if not found:
            print("Password not found.\n")

def view_all():
    if not os.path.exists(FILENAME):
        print("No passwords saved yet.\n")
        return
    
    print("Saved Passwords")
    print("-" * 30)

    with open(FILENAME, "r") as f:
        
        for line in f:
            data = parse_line(line)
            if not data:
                continue

            stored_site, stored_username, stored_password = data

            print(f"Website: {stored_site} | Username: {stored_username}")

    print("-" * 30)

def update_password():
    website = input("Enter website").strip()
    username = input("Enter username").strip()

    if not os.path.exists(FILENAME):
        print("No passwords saved yet.\n")
        return
    
    lines = []
    found = False

    with open(FILENAME,"r") as f:

        for line in f:
            data = parse_line(line)
            if not data:
                continue

            stored_site, stored_username, stored_password = data

            if stored_site.lower() == website.lower() and stored_username.lower() == username.lower():
                new_password = input("Enter new password: ").strip()
                lines.append(f"{stored_site},{stored_username},{new_password}\n")
                found = True    
            else:
                lines.append(line)
    if found:

        with open(FILENAME,"w") as f:
            f.writelines(lines)

            print("Password saved successfully.\n")

    else:
        print("No matching account found.\n")

def delete_password():
    website = input("Enter website").strip()
    username = input("Enter username").strip()

    if not os.path.exists(FILENAME):
        print("No passwords saved yet.\n")
        return
    
    lines = []
    found = False

    with open(FILENAME,"r") as f:

        for line in f:
            data = parse_line(line)
            if not data:
                continue

            stored_site, stored_username, stored_password = data

            if stored_site.lower() == website.lower() and stored_username.lower() == username.lower():
                found = True

            else:
                lines.append(line)

    if found:

        with open(FILENAME, "w") as f:
            f.writelines(lines)

        print("Password deleted successfully.\n")

    else:
        print("No matching account found.\n")

def search_password():
    search = input("Enter search term: ").strip()

    found = False

    if not os.path.exists(FILENAME):
        print("No file exists yet.\n")
        return
    
    with open(FILENAME, "r") as f:

        for line in f:
            data = parse_line(line)
            if not data:
                continue

            stored_site, stored_username, stored_password = data

            if search.lower() in stored_site.lower() or search.lower() in stored_username.lower():
                print(f"Website: {stored_site}")
                print(f"Username: {stored_username}")
                print()
                found = True

        if not found:
            print("Nothing matches try again.\n")


def main():
    
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. View Password")
        print("3. View All Passwords")
        print("4. Update Password")
        print("5. Delete Password")
        print("6. Search Password")
        print("7. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_password()
        elif choice == "2":
            view_password()
        elif choice == "3":
            view_all()
        elif choice == "4":
            update_password()
        elif choice == "5":
            delete_password()
        elif choice == "6":
            search_password()
        elif choice == "7":
            break

        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
