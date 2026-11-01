import os

FILENAME = "journal.txt"


def show_menu():
    print("Welcome to Personal Journal Manager!")
    print("Please select an option:")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")


def new_entry():
    print("--- Add a New Entry ---")
    entry = input("Enter your journal entry:")
    with open(FILENAME, "a") as file:
        file.write(entry + "\n---\n")
    print("Entry added successfully!")


def view_entries():
    print("--- All Journal Entries ---")
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        print("No entries found.")
        return

    with open(FILENAME, "r") as file:
        content = file.read()
        print(content)


def search_entry():
    print("--- Search Entries ---")
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        print("No entries found.")
        return

    keyword = input("Enter a keyword to search for: ").lower()
    found = False

    with open(FILENAME, "r") as file:
        entries = file.read().split("---")
        for i, entry in enumerate(entries, 1):
            if keyword in entry.lower() and entry.strip():
                print(f"\n[Match Found]:\n{entry.strip()}")
                found = True

    if not found:
        print("No matching entries found.")


def delete_all_entries():
    confirm = input("Are you sure you want to delete all entries? (y/n): ")
    if confirm.lower() == "y":
        open(FILENAME, "w").close()  # Overwrites file with empty contents
        print("All entries deleted successfully!")
    else:
        print("Deletion canceled.")


def main():
    while True:
        show_menu()
        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            new_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entry()
        elif choice == "4":
            delete_all_entries()
        elif choice == "5":
            print("Exiting Personal Journal Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()