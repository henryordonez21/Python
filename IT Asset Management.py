import os

FILENAME = "asset_management.txt"

def load_assets():
    assets = []
    if not os.path.exists(FILENAME):
        print("No asset file found. Starting with empty inventory.")
        return assets
    
    with open(FILENAME, "r") as f:
        for line in f:
            parts = line.strip().split(",")

            device_name = parts[0]
            assigned_user = parts[1]
            department = parts[2]
            status = parts[3]

            asset = {

                "device_name" :device_name,
                "assigned_user":assigned_user,
                "department": department,
                "status": status
            }

            assets.append(asset)
    return assets

def save_assets(assets):
        
    with open(FILENAME, "w") as f:

        for asset in assets:

            f.write(f"{asset['device_name']},{asset['assigned_user']},{asset['department']},{asset['status']}\n")


def add_asset(assets):
    device_name = input("Enter device name: ").strip()

    for asset in assets:
        if asset["device_name"] == device_name:
            print("Asset already exists.")
            return
    
    assigned_user = input("Enter assigned user: ").strip()
    department = input("Enter department: ").strip()
    status = input("Enter user status: ").strip()

    asset = {
        "device_name" : device_name,
        "assigned_user": assigned_user,
        "department": department,
        "status":   status
      }

    assets.append(asset)
    save_assets(assets)

    print("Asset added successfully.")

def display_assets(assets):
   
    if len(assets) == 0:

        print("No assets exist.")
        return
    
    for asset in assets:
        print("Device Name:", asset["device_name"])
        print("Assigned User:", asset["assigned_user"])
        print("Department:", asset["department"])
        print("Status:", asset["status"])
        print()

def search_assets(assets):

    device_search = input("Enter device name").strip()

    found = False

    for asset in assets:

        if device_search == asset["device_name"]:

            found = True
            print("Device Name:", asset["device_name"])
            print("Assigned User:", asset["assigned_user"])
            print("Department:", asset["department"])
            print("Status:", asset["status"])
            print()
            break
    
    if not found:
        print("Asset not found")


def delete_asset(assets):

    device_search = input("Enter device name: ").strip()

    found = False

    for asset in assets:

        if device_search == asset["device_name"]:

            found = True

            assets.remove(asset)
            save_assets(assets)

            print("Asset deleted successfully.")
            break
        
    if not found:
        print("Asset not found")

def main():
    assets = load_assets()
    while True:
        print("1. Add Assets")
        print("2. Display Assets")
        print("3. Search")
        print("4. Delete Asset")
        print("5. Exit")

        choice = input("Choose an option: \n")

        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            display_assets(assets)
        elif choice == "3":
            search_assets(assets)
        elif choice == "4":
            delete_asset(assets)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()