FILENAME = ("passwords.txt")

def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    with open(FILENAME, "a") as f:
        f.write(f"{website},{username},{password}\n")

print("Saved!")

def view_password():
    website = input("Enter website: ").strip()
    found = False

    with open(FILENAME,"r") as f:
        for line in f:
            stored_site,username,password = line.strip().split(",")

        if stored_site == website:
            print("Username",username)
            print("Password",password)
            print()
            found = True
    if not found:
        print("Website not found")

while True:
    print("\n1. Add Password")
    print("2. View Password")
    print("3. Quit")

    answer = input("Choose an option: ")

    if answer == "1":
        add_password()
    elif answer == "2":
        view_password()
    elif answer == "3":
        break
    else:
        print("Invalid Number")


        
