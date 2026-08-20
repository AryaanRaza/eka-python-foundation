import knowledge_tools


title = input("Enter title: ")
content = input("Enter content: ")
category = input("Enter category: ")
source = input("Enter source: ")

item = knowledge_tools.create_knowledge(
    title,
    content,
    category,
    source
)

if item is not None:
    print("\nKnowledge created:")
    print(item)

else:
    print("\nInvalid knowledge.")