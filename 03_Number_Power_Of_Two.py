def isPowerOfTwo(num):
    # Check if the number is greater than 0 and (num & (num - 1)) equals 0
    return num > 0 and (num & (num - 1)) == 0


num = int(input("Enter a number: "))
if isPowerOfTwo(num):
    print(f"{num} is Power of 2")
else:
    print(f"{num} is not power of 2")
