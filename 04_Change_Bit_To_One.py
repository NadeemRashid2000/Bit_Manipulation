# Changing from the left side
# Formula = number|(1 << position)


"""
a = 8
b = 1
b = b << 2
print(b)
print(a|b)

"""
def changeBit(num, pos, bit):
    if bit == 1:
        num |= 1 << pos  # Set bit to 1
    else:
        num &= ~(1 << pos)  # Set bit to 0
    return num


num = int(input("Enter a number: "))
pos = int(input("Enter position of bit to change: "))
bit = int(input("Enter the bit value (0 or 1): "))
num = changeBit(num, pos, bit)
print(f"Updated number: {num}")
