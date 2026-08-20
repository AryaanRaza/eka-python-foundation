# Creates and returns one knowledge dictionary.
def create_knowledge(title, content, category, source):

    if title == "":
        return None

    if content == "":
        return None

    if category == "":
        return None

    knowledge_item = {
        "title": title,
        "content": content,
        "category": category,
        "source": source
    }

    return knowledge_item