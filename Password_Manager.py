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
    website =  input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    with open(FILENAME, "r") as f:
        found = False
        for line in f:
            data = parse_line(line)
            if not data:
                continue

            file_website, file_username, _ = data
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
            data = parse_line(line)
            if not data:
                continue

            stored_site, username, password = data

            if stored_site.lower() == website.lower():
                print(f"Username: {username}")
                print(f"Password: {password}")
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
            data = parse_line(line)
            if not data:
                continue
            website, username, password = data
            print(f"Website: {website} | Username: {username}")

    print("-" * 30)

def update_password():
    website = input("Enter Website to update: \n")
    username = input("Enter Username to update: \n")

    if not os.path.exists(FILENAME):
        print("No passwords saved yet. \n")
        return
    
    lines = []
    found = False

    with open(FILENAME, "r") as f:
        for line in f:
            data = parse_line(line)
            if not data:
                continue
            stored_site, file_username, password = data

            if stored_site.lower() == website.lower() and file_username.lower() == username.lower():
                new_password = input("Enter new password: ").strip()
                lines.append(f"{stored_site},{file_username},{new_password}\n")
                found = True
            else:
                lines.append(f"{stored_site},{file_username},{password}\n")
                
    with open(FILENAME, "w") as f:
        f.writelines(lines)

    if found:
        print("Password updated.\n")
    else:
        print("No entry found for that website/username.\n")


def delete_password():
    website = input("Enter website to delete: \n").strip()

    if not os.path.exists(FILENAME):
        print("No passwords saved yet. \n")
        return
    
    lines = []
    found = False

    with open(FILENAME, "r") as f:
        for line in f:
            data = parse_line(line)
            if not data:
                continue
            stored_site, username, password = data

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
            data = parse_line(line)
            if not data:
                continue
            stored_site, username, password = data

            if stored_site.lower() == website.lower():
                print(f"Username: {username}")
                print(f"Password: {password}")
                print()
                found = True

    if not found:
            print("No password found for this website.\n")

def main():

    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. View Password")
        print("3. View All Passwords")
        print("4. Delete Password")
        print("5. Search Passwords")
        print("6. Update Password")
        print("7. Quit")

        choice = input("Choose an option: ").strip()

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
            update_password()
        elif choice == "7":
            break
        else:
            print("Not a valid input")
if __name__ == "__main__":
    main()



           

            
