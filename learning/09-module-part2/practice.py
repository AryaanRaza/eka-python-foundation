import storage_tools


knowledge = [
    {
        "title": "Leave Policy",
        "content": "Employees receive 20 days annual leave.",
        "category": "HR",
        "source": "Company Handbook"
    }
]


# Save the knowledge to a JSON file.
storage_tools.save_data(
    knowledge,
    "practice_knowledge.json"
)


print("Knowledge saved.")


# Load the knowledge back from the JSON file.
loaded_knowledge = storage_tools.load_data(
    "practice_knowledge.json"
)


print("\nLoaded knowledge:")
print(loaded_knowledge)