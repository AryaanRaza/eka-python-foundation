# A dictionary stores related information using key-value pairs.
# Each key describes what the value represents.

knowledge = {
    "title": "Leave Policy",
    "content": "Employees receive 20 days annual leave.",
    "category": "HR"
}

# Access a value by using its key.
print(knowledge["title"])
print(knowledge["content"])
print(knowledge["category"])

# Chaning Dictionary data
knowledge["category"] = "Human Resources"
knowledge["author"] = "Admin"
print(knowledge)



# Create a dictionary representing one employee.
employee = {
    "name": "Arjun",
    "department": "Engineering",
    "role": "Software Developer"
}

# Display individual pieces of information using their keys.
print("Employee:", employee["name"])
print("Department:", employee["department"])
print("Role:", employee["role"])

# Add a new piece of information to the dictionary.
employee["experience"] = 2

print("Experience:", employee["experience"])