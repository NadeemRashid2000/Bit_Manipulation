def countOnes(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count


num = int(input("Enter a number: "))
print(f"Number of 1s: {countOnes(num)}")
