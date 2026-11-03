# Tuples and Sets

# Tuple: Ordered and immutable
coordinates = (41.0082, 28.9784)

print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])

# Set: Stores unique values
numbers = {1, 2, 2, 3, 4, 4, 5}

print("Unique numbers:", numbers)

# Add and remove items
numbers.add(6)
numbers.discard(3)

print("Updated set:", numbers)
