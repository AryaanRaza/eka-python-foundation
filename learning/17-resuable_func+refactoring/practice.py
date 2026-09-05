def save_result(name = "black" , score ="9"):
    print(f"Name: {name}")
    print(f"Score: {score}")
    print("\n")

save_result()
save_result("rider" , "04")
save_result("rider")


def display_user(name , role , status = "active"):
    print(f"Name: {name}")
    print(f"Role: {role}")
    print(f"Status: {status}")
    print("\n")

display_user("balck" , "Developer")
display_user("balck" , "Developer" , "offline")


def calculate_total(price , quantity):
    amt = price * quantity
    return amt

print(f"Amount: {calculate_total(12 , 30)}")