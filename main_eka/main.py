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
    print("3. Search Knowledge")
    print("4. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        title = input("Enter knowledge title: ")
        content = input("Enter knowledge: ")
        category = input("Enter knowledge category: ")
        source = input("Enter knowledge source: ")
        knowledge_item = knowledge.create_knowledge(title, content, category, source)

        if knowledge_item is not None:
            knowledge_items.append(knowledge_item)
            # Save immediately after adding knowledge.
            saved = storage.save_data(knowledge_items, "main_eka/knowledge.json")
            if saved:
                print("Knowledge added and saved.")
            else:
                print("Knowledge added, but could not be saved.")

    elif choice == "2":
        knowledge.display_knowledge(knowledge_items)

    elif choice == "3":
        search_text = input("Enter the knowledge keyword you want to search for: ")
        field_choices = {
            "1": "all",
            "2": "title",
            "3": "content",
            "4": "category",
            "5": "source",
        }
        print("Search in : \n")
        print("1. All fields")
        print("2. Title")
        print("3. Content")
        print("4. Category")
        print("5. Source")
        field = input("Your choice: ")
        field_search = field_choices.get(field)

        if field_search is None:
            print("Invalid search field. Please choose 1, 2, 3, 4 or 5.")
            continue
        else:
            search_results = knowledge.search_knowledge(
                knowledge_items, search_text, field_search
            )

        if len(search_results) != 0:
            knowledge.display_knowledge(search_results)

    elif choice == "4":
        print("Exiting EKA...")
        break

    else:
        print("Invalid option . Please choose 1 , 2  , 3 or 4.")
