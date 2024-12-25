def swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = swap(a, b)
print(f"Swapped: a = {a}, b = {b}")
