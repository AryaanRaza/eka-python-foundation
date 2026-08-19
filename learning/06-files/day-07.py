# Open a file in write mode.
# If the file does not exist, Python creates it.
with open("learning/knowledge.txt", "w") as file:

    # Write text into the file.
    file.write("EKA is learning to remember information.")


# Open the file in read mode.
with open("learning/knowledge.txt", "r") as file:

    # Read everything from the file.
    content = file.read()

# Display the content.
print(content)


# Open the file in append mode.
# Append means add new information without deleting existing information.
with open("learning/knowledge.txt", "a") as file:

    file.write("\nPython can work with files.")