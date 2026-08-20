import knowledge
import storage
project_name = "Enterprise Knowledge Assistant"
version = "0.8"

# Load previously saved knowledge when EKA starts.
knowledge_items = storage.load_data("main_eka/knowledge.json")

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
            saved = storage.save_data(knowledge_items,"main_eka/knowledge.json")
            if saved:
                print("Knowledge added and saved.")
            else:
                print("Knowledge added, but could not be saved.")


    elif choice == "2":
        knowledge.display_knowledge(knowledge_items)

    elif choice == "3":
        print("Exiting EKA...")
        break

    else:
        print("Invalid option . Please choose 1 , 2 or 3.")