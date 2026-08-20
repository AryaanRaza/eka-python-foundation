import json


# Saves data into a JSON file.
def save_data(data, filename):

    try:

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        return True

    except OSError:

        return False


# Loads data from a JSON file.
def load_data(filename):

    try:

        with open(filename, "r") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:

        return []

    except json.JSONDecodeError:

        return []