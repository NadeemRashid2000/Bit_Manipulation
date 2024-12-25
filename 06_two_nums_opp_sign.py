def haveOppositeSigns(a, b):
    return (a ^ b) < 0


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if haveOppositeSigns(a, b):
    print("Opposite signs")
else:
    print("Same sign")
