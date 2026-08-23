# Creates and validates a knowledge item.
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

def display_knowledge(knowledge_items):
        print("\n=== EKA Knowledge Base ===")
        if len(knowledge_items) == 0:
            print("No knowledge available")

        else:
            for item in knowledge_items:
                print("\nTitle:", item["title"])
                print("Content:", item["content"])
                print("Category:", item["category"])
                print("Source:", item["source"])

def search_knowledge(knowledge_items , search_text):

    search_text = search_text.strip().lower()

    if search_text == "":
        print("Search cannot be empty")
        return []


    matching_items = []

    for knowledge_item in knowledge_items:
            # Check if the search text is present in any value of the knowledge dictionary.
            # item.values() gives all dictionary values (title, content, category, source).
            # str(value).lower() converts each value to lowercase for case-insensitive searching.
            # any() returns True if the search text is found in at least one value.
            if any(search_text in str(value).lower() for value in knowledge_item.values()):
                matching_items.append(knowledge_item)

    if matching_items:
        print("Knowledge is present in the following texts")
    else:
        print("Given knowledge is not present")
        
    return matching_items
    
