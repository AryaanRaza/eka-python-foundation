while True:

    print("\n=== MENU ===")
    print("1. Add Knowledge")
    print("2. View Knowledge")
    print("3. Exit")

    try:

        choice = int(input("Choose an option: "))

    except ValueError:

        print("Please enter 1, 2, or 3.")
        continue

    if choice == 1:

        print("Add knowledge selected.")

    elif choice == 2:

        print("View knowledge selected.")

    elif choice == 3:

        print("Goodbye!")
        break

    else:

        print("Invalid option.")