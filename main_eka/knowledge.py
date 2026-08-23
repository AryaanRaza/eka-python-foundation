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

    found = False
    presentIn = []

    for item in knowledge_items:
        if search_text in item["title"].lower():
            found = True
            presentIn.append(item)

    if found:
        print("Knowledge is present in the following texts")
    else:
        print("Given knowledge is not present")
        
    return presentIn
    
