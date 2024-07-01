A1
# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    num = input()  # Read the number as a string
    sum_of_digits = 0
    # Iterate over each character using string slicing
    for i in range(len(num)):
        sum_of_digits += int(num[i])
    print(sum_of_digits)

A2
T=int(input())
for i in range(T):
    num=int(input())
    sum=0
    for j in str(num):
        sum+=int(j)
    print(sum)
    
A3
t = int(input())
for i in range(t):
    num = int(input())
    ans = 0
    while num!=0:
        curr_dig = num % 10
        ans = ans + curr_dig
        num = num // 10 
    print(ans)
