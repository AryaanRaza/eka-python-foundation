# A dictionary represents one knowledge record.
knowledge = {
    "title": "Python Functions",
    "content": "Functions help us organize reusable code.",
    "category": "Python",
    "source": "Python Documentation"
}

# This variable represents the field we want to inspect.
field_choices = {
    "1" : "title",
    "2" : "content",
    "3" : "category",
    "4" : "source"
}
print("Enter 1 for title")
print("Enter 2 for content")
print("Enter 3 for category")
print("Enter 4 for source")
choice = input("Your choice: ")
field = field_choices[choice]

# Instead of writing knowledge["title"] directly,
# we use the field variable to decide which dictionary value to access.
if choice == "1":
    print("Selected value:", knowledge[field])

elif choice == "2":
    print("Selected value:", knowledge[field])

elif choice == "3":
    print("Selected value:", knowledge[field])

elif choice == "4":
    print("Selected value:", knowledge[field])

else:
    print("Wrong entry choose from 1 , 2 or 3")


