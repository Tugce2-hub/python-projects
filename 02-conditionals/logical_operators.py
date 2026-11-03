# Logical Operators

age = 22
has_ticket = True

# AND: Both conditions must be True
if age >= 18 and has_ticket:
    print("You can enter.")

# OR: At least one condition must be True
if age >= 18 or has_ticket:
    print("At least one condition is True.")

# NOT: Reverses the Boolean value
if not has_ticket:
    print("You need a ticket.")
else:
    print("Your ticket is ready.")
