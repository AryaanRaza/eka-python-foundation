import json
import knowledge
project_name = "Enterprise Knowledge Assistant"
version = "0.7"

knowledge_items = []

def save_knowledge():

    try:

        # Open the knowledge file in write mode.
        with open("knowledge.json", "w") as file:
            # Convert the Python knowledge list into JSON.
            json.dump(knowledge_items, file, indent=4)
    except OSError:
        print("Error: Could not save knowledge. ")


def load_knowledge():

    global knowledge_items

    try:

        # Open the existing knowledge file.
        with open("knowledge.json", "r") as file:

            # Convert JSON back into Python data.
            knowledge_items = json.load(file)

    except FileNotFoundError:

        # If this is the first time EKA is running,
        # there may not be a knowledge file yet.
        print("No knowledge file found. Starting with empty knowledge.")
        knowledge_items = []

    except json.JSONDecodeError:
        print("Knowledge file is corrupted.")
        print("Starting with empty knowledge.")
        knowledg_items = []

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
        knowledge_item = knowledge.create_knowledge(title , content , category , source)

        if(knowledge_item is not None):
            knowledge_items.append(knowledge_item)
            # Save immediately after adding knowledge.
            save_knowledge()
            print("Knowledge added succesfully")

    elif choice == "2":
        knowledge.display_knowledge(knowledge_items)

    elif choice == "3":
        print("Exiting EKA...")
        break

    else:
        print("Incalid option . Please choose 1 , 2 or 3.")