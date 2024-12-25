def reverseBits(num):
    reversed = 0
    while num:
        reversed = (reversed << 1) | (num & 1)
        num >>= 1
    return reversed


num = int(input("Enter a number: "))
print(f"Reversed bits: {reverseBits(num)}")
