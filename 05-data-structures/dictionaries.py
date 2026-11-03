# Python Dictionaries

student = {
    "name": "Tugce",
    "age": 24,
    "department": "Management Information Systems"
}

# Access values
print("Name:", student["name"])
print("Age:", student["age"])

# Add a new key-value pair
student["city"] = "Istanbul"

# Update a value
student["age"] = 25

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)
