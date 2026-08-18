project_name = "Enterprise Knowledge Assistant"
version = "0.3"

knowledge = []

def create_knowledge(title , content , category , source):

    if title == "":
        print("Title cannot be empty.")
        return None

    if content == "":
        print("Error: Content cannot be empty.")
        return None

    if category == "":
        print("Error: Category cannot be empty.")
        return None

    knowledge_item = {
        "title": title,
        "content": content,
        "category": category,
        "source": source,
    }
    return knowledge_item


print("=" * 40)
print(project_name)
print(f"Version: {version}")
print("=" * 40)

for i in range(2):
    print(f"\nKnowledge #{i + 1}")

    title = input("Enter knowledge title: ")
    content = input("Enter knowledge: ")
    category = input("Enter knowledge category: ")
    if category == "HR":
        print("Category recognized: Human Resources")

    elif category == "IT":
        print("Category recognized: Information Technology")
    else:
        print("Category: General")
    source = input("Enter knowledge source: ")

    knowledge_item = create_knowledge(title , content , category , source)
    if(knowledge_item is not None):
        knowledge.append(knowledge_item)

print("\n=== EKA Knowledge Base ===")

for item in knowledge:
    print("\nTitle:", item["title"])
    print("Content:", item["content"])
    print("Category:", item["category"])
    print("Source:", item["source"])