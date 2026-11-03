# Default Parameters

def greet(name="Guest"):
    print("Hello,", name)

def calculate_discount(price, discount=10):
    final_price = price - (price * discount / 100)
    return final_price

greet()
greet("Tugce")

print("Discounted Price:", calculate_discount(100))
print("Discounted Price:", calculate_discount(100, 20))
