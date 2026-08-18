project_name = "Enterprise Knowledge Assistant"
version = "0.3"

knowledge = []

print("=" * 40)
print(project_name)
print(f"Version: {version}")
print("=" * 40)

for i in range(3):
    print(f"\nKnowledge #{i + 1}")

    title = input("Enter knowledge title: ")
    content = input("Enter knowledge: ")
    category = input("Enter knowledge category: ")

    knowledge_item = {
        "title": title,
        "content": content,
        "category": category
    }
    knowledge.append(knowledge_item)

print("\n=== EKA Knowledge Base ===")

for item in knowledge:
    print("\nTitle:", item["title"])
    print("Category:", item["category"])
    print("Content:", item["content"])