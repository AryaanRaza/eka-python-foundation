# A while loop allows the program to keep running
# until we explicitly decide to stop it.

while True:

    print("\n=== EKA MENU ===")
    print("1. Add knowledge")
    print("2. View knowledge")
    print("3. Exit")

    choice = input("Choose an option: ")

    # If the user chooses 3, stop the loop.
    if choice == "3":
        print("Goodbye!")
        break

    # Otherwise, tell the user what they selected.
    print(f"You selected option {choice}.")