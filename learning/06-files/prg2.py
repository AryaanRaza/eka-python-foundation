import json

knowledge = [
    {
        "title": "Leave Policy",
        "content": "Employees receive 20 days annual leave.",
        "category": "HR",
        "source": "Company Handbook"
    }
]

# Open the JSON file in write mode.
with open("learning/06-files/knowledge.json", "w") as file:

    # Convert the Python list/dictionaries into JSON.
    json.dump(knowledge, file, indent=4)



# Open the saved JSON file.
with open("learning/06-files/knowledge.json", "r") as file:

    # Convert JSON back into Python data.
    knowledge = json.load(file)

print(knowledge)