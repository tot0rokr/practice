import json

# Define a Python dictionary
people = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 32,
    "city": "New York"
}
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 32,
    "city": "New York"
}
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 32,
    "city": "New York"
}

# Encode the dictionary into a JSON string
person_json = json.dumps(person)

# Print the JSON string
print("JSON encoded string: ", person_json)

# Decode the JSON string back into a Python object
person_obj = json.loads(person_json)

# Print the decoded Python object
print("\nDecoded Python object: ", person_obj)
