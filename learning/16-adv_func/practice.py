# The message parameter has a default value.
# If the caller does not provide a message,
# Python automatically uses "Hello".

def greet(name, message="Hello"):
    print(message, name)


# No message is provided,
# so the default "Hello" is used.
greet("Alex")


# A message is provided,
# so it replaces the default value.
greet("Alex", "Good morning")