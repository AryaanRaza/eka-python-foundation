import json
project_name = "Enterprise Knowledge Assistant"
version = "0.3"

knowledge = []

def create_knowledge(title , content , category , source):

    if title == "":
        print("Error: Title cannot be empty.")
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

def save_knowledge():

    # Open the knowledge file in write mode.
    with open("knowledge.json", "w") as file:

        # Convert the Python knowledge list into JSON.
        json.dump(knowledge, file, indent=4)


def load_knowledge():

    global knowledge

    try:

        # Open the existing knowledge file.
        with open("knowledge.json", "r") as file:

            # Convert JSON back into Python data.
            knowledge = json.load(file)

    except FileNotFoundError:

        # If this is the first time EKA is running,
        # there may not be a knowledge file yet.
        knowledge = []


# Load previously saved knowledge when EKA starts.
load_knowledge()

print("=" * 40)
print(project_name)
print(f"Version: {version}")
print("=" * 40)


while True:
    print("\n=== EKA MENU ===")
    print("1. Add Knowledge")
    print("2. View Knowledge")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter knowledge title: ")
        content = input("Enter knowledge: ")
        category = input("Enter knowledge category: ")
        source = input("Enter knowledge source: ")
        knowledge_item = create_knowledge(title , content , category , source)

        if(knowledge_item is not None):
            knowledge.append(knowledge_item)
            # Save immediately after adding knowledge.
            save_knowledge()
            print("Knowledge added succesfully")

    elif choice == "2":
        print("\n=== EKA Knowledge Base ===")
        if len(knowledge) == 0:
            print("No knowledge available")

        else:
            for item in knowledge:
                print("\nTitle:", item["title"])
                print("Content:", item["content"])
                print("Category:", item["category"])
                print("Source:", item["source"])
            
    elif choice == "3":
        print("Exiting EKA...")
        break

    else:
        print("Incalid option . Please choose 1 , 2 or 3.")