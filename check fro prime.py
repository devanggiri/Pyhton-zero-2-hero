# n = int(input("Enter a number: "))

# # Initial check for numbers less than 2
# if n < 2:
#     print("Not Prime")
# else:
#     num = 2
#     while num * num <= n:
#         if n % num == 0:
#             print("Not Prime")
#             break
#         num += 1
#     else:
#         print("Prime")
n = int(input("Enter a number: "))

# Initial check for numbers less than 2
if n > 1:
    #for x in range(2, n):
    for x in range(2, (n//2) + 1):
        if (n%x) == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")
