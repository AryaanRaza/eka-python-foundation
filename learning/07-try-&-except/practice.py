
user_input = input("Enter a number: ")

try:
    number = int(user_input)
    print("You entereed a number")

except ValueError:
    print("Please enter a valid number.")


try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print("Number accepted:", number)
finally:
    print("Program finished this operation.")

# | Exception           | Example                      |
# | ------------------- | ---------------------------- |
# | `ValueError`        | Invalid value conversion     |
# | `FileNotFoundError` | File doesn't exist           |
# | `KeyError`          | Dictionary key doesn't exist |
# | `IndexError`        | List index doesn't exist     |
# | `TypeError`         | Wrong type of data           |
