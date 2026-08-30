# A list can contain multiple dictionaries.
# Each dictionary represents one knowledge item.

knowledge_items = [
    {
        "title": "Python Basics",
        "content": "Python is a programming language.",
        "category": "Programming",
        "source": "Python Docs"
    },
    {
        "title": "Machine Learning",
        "content": "Machine learning allows computers to learn from data.",
        "category": "AI",
        "source": "Course Notes"
    }
]


# Access the first knowledge item.
first_item = knowledge_items[0]

print("First knowledge item:")
print(first_item)


# Access only the title from the first item.
print("\nFirst title:")
print(first_item["title"])


# Create a separate list containing only the titles.
titles = []

for item in knowledge_items:
    titles.append(item["title"])

print("\nAll titles:")
print(titles)