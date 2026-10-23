import json

data = {
    "name": "tester",
    "age": 25,
    "email": "mam@gmail.com"
}

with open(r"C:\Users\User\Desktop\14187267426000002\file.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data saved successfully!")