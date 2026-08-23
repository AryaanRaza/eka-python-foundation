# A list can contain multiple pieces of text that we want to search through.
knowledge = [
    "Python is a programming language",
    "Machine learning uses data to learn patterns",
    "Python functions help organize code",
    "Databases store information"
]

# input() lets the user provide the word or phrase they want to search for.
search = input("What do you want to search for? ")

# strip() removes accidental spaces from the beginning and end.
# lower() makes the search case-insensitive.
search = search.strip().lower()

# Track if we found at least one match.
found_any = False

# We check each knowledge item one at a time.
for item in knowledge:
    # lower() also converts the knowledge item to lowercase.
    # 'in' checks whether the search text exists inside the item.
    if search in item.lower():
        # This runs when a matching item is found.
        print("Found:", item)
        found_any = True  # Mark that we found a match

# This runs after checking everything, only if no matches were found.
if not found_any:
    print("No matching knowledge found")
