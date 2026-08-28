# Creates and validates a knowledge item.
def create_knowledge(title, content, category, source):

    if title == "":
        print("Error: Title cannot be empty.")
        return None

    if content == "":
        print("Error: Content cannot be empty.")
        return None

    if category == "":
        print("Error: Category cannot be empty.")
        return None
    
    if source == "":
        print("Error: Source cannot be empty.")
        return None

    knowledge_item = {
        "title": title,
        "content": content,
        "category": category,
        "source": source,
    }
    return knowledge_item


def delete_knowledge(knowledge_items):

    # Check if the knowledge base is empty before asking the user for a number.
    if len(knowledge_items) == 0:
        print("No knowledge available")
        return knowledge_items

    try:
        # Take the knowledge number displayed to the user and convert it to an integer.
        knowledge_number = int(
            input("Enter the number of the knowledge to delete: ")
        )

    except ValueError:
        # Handle cases where the user enters something that is not a valid number.
        print("Invalid number.")
        return knowledge_items

    # Make sure the selected number corresponds to an existing knowledge item.
    if knowledge_number < 1 or knowledge_number > len(knowledge_items):
        print(f"Invalid number. Choose a number between 1 - {len(knowledge_items)}")
        return knowledge_items

    # Python list indexes start from 0, while the user sees knowledge numbers starting from 1.
    # Subtract 1 to convert the user's number into the correct list index.
    knowledge_items.pop(knowledge_number - 1)

    # Return the updated knowledge list to main.py.
    return knowledge_items



def update_knowledge(knowledge_items):

    # Check whether there is any knowledge available to update.
    if len(knowledge_items) == 0:
        print("No knowledge available.")
        return knowledge_items

    # Display all knowledge items with numbers so the user
    # can select which record they want to update.
    print("\n=== Select Knowledge to Update ===")

    for index, item in enumerate(knowledge_items):
        print(f"{index + 1}. {item['title']}")

    # Ask the user which knowledge item they want to update.
    try:
        choice = int(input("Enter the number of the knowledge to update: "))

        # The user sees numbers starting from 1,
        # but Python list indexes start from 0.
        if choice < 1 or choice > len(knowledge_items):
            print("Invalid knowledge number.")
            return knowledge_items

        # Convert the user's number into the correct list index.
        knowledge_item = knowledge_items[choice - 1]

        print("\n=== Current Knowledge ===")
        print("Title:", knowledge_item["title"])
        print("Content:", knowledge_item["content"])
        print("Category:", knowledge_item["category"])
        print("Source:", knowledge_item["source"])

        print("\nPress Enter if you want to keep the current value.")

        # Ask for the new values.
        new_title = input("New title: ").strip()
        new_content = input("New content: ").strip()
        new_category = input("New category: ").strip()
        new_source = input("New source: ").strip()

        # Only update a field if the user entered something.
        # Pressing Enter keeps the existing value.
        if new_title != "":
            knowledge_item["title"] = new_title

        if new_content != "":
            knowledge_item["content"] = new_content

        if new_category != "":
            knowledge_item["category"] = new_category

        if new_source != "":
            knowledge_item["source"] = new_source

        print("\nKnowledge updated successfully.")

    except ValueError:
        # int() raises ValueError if the user enters something
        # that cannot be converted into a number.
        print("Invalid input. Please enter a number.")

    return knowledge_items



def display_knowledge(knowledge_items):
    print("\n=== EKA Knowledge Base ===")
    if len(knowledge_items) == 0:
        print("No knowledge available")

    else:
        for index , item in enumerate(knowledge_items , start = 1):
            print("\n\n     Knowledge " , index)
            print("Title:", item["title"])
            print("Content:", item["content"])
            print("Category:", item["category"])
            print("Source:", item["source"])


def search_knowledge(knowledge_items, search_text, search_field):

    search_text = search_text.strip().lower()

    if search_text == "":
        print("Search cannot be empty")
        return []

    matching_items = []

    for knowledge_item in knowledge_items:

        if(search_field == "all"):
        # Check if the search text is present in any value of the knowledge dictionary.
        # item.values() gives all dictionary values (title, content, category, source).
        # str(value).lower() converts each value to lowercase for case-insensitive searching.
        # any() returns True if the search text is found in at least one value.
            if any(search_text in str(value).lower() for value in knowledge_item.values()):
                matching_items.append(knowledge_item)
        else:
            if(search_text in knowledge_item[search_field].lower()):
                matching_items.append(knowledge_item)

    if matching_items:
        print("Knowledge is present in the following texts")
    else:
        print("Given knowledge is not present")

    return matching_items
