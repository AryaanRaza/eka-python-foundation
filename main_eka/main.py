project_name = "Enterprise Knowledge Assistant"
version = "0.2"

knowledge = []

print("=" * 40)
print(project_name)
print(f"Version: {version}")
print("=" * 40)

for i in range(3):
    print(f"\nKnowledge #{i + 1}")

    title = input("Enter knowledge title: ")
    content = input("Enter knowledge: ")

    knowledge.append({
        "title": title,
        "content": content
    })

print("\n=== EKA Knowledge Base ===")

for item in knowledge:
    print("\nTitle:", item["title"])
    print("Content:", item["content"])