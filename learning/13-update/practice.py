# A dictionary represents one knowledge record.
knowledge = {
    "title": "Python",
    "content": "Python is a programming language.",
    "category": "Programming",
    "source": "Python Documentation"
}

print("Before update:")
print(knowledge)

# A dictionary value can be changed by assigning a new value
# to the same key.
knowledge["title"] = "Python Programming"

print("\nAfter update:")
print(knowledge)

