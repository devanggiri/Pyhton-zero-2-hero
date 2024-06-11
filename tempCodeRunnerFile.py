#odd rane
n = int(input("Enter a number: "))
if n < 1:
    print("0 is invalid")
else:
    for x in range(1, n + 1):
        if x % 2 != 0:  # Check if the number is odd
            print(x)