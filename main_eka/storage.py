import json
def save_data(data , filename):

    try:

        # Open the knowledge file in write mode.
        with open(filename, "w") as file:
            # Convert the Python knowledge list into JSON.
            json.dump(data, file, indent=4)
            return True
    except OSError:
        print("Error: Could not save knowledge. ")
        return False

def load_data(filename):

    try:
        # Open the existing knowledge file.
        with open(filename, "r") as file:
            # Convert JSON back into Python data.
            data = json.load(file)
            return data

    except FileNotFoundError:
        # If this is the first time EKA is running,
        # there may not be a knowledge file yet.
        print("No knowledge file found. Starting with empty knowledge.")
        return []

    except json.JSONDecodeError:
        print("Knowledge file is corrupted.")
        return []