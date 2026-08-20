import json

# This list represents the knowledge currently held by our program.
knowledge = []


# Add one piece of knowledge to the list.
knowledge.append({
    "title": "Leave Policy",
    "content": "Employees receive 20 days annual leave.",
    "category": "HR",
    "source": "Company Handbook"
})


# Save the knowledge list into a JSON file.
with open("learning/06-files/practice_knowledge.json", "w") as file:

    # Convert Python data into JSON format.
    json.dump(knowledge, file, indent=4)


print("Knowledge saved!")


# Open the JSON file again.
with open("learning/06-files/practice_knowledge.json", "r") as file:

    # Convert the JSON data back into Python data.
    loaded_knowledge = json.load(file)


print("\nLoaded Knowledge:")

for item in loaded_knowledge:

    print("\nTitle:", item["title"])
    print("Content:", item["content"])
    print("Category:", item["category"])
    print("Source:", item["source"])