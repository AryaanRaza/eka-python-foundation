# A function groups code that performs one specific task.
def show_welcome():
    print("=" * 40)
    print("Welcome to Enterprise Knowledge Assistant")
    print("=" * 40)


# This function receives a name and uses it inside the function.
def greet_user(name):
    print(f"Hello, {name}!")


# Call the functions to execute their code.
show_welcome()

name = input("Enter your name: ")

greet_user(name)