def findSingleNumber(arr):
    result = 0
    for num in arr:
        result ^= num
    return result


size = int(input("Enter the size of the array: "))
arr = [int(input(f"Enter element {i + 1}: ")) for i in range(size)]
print(f"Single number: {findSingleNumber(arr)}")
