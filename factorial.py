n = int(input())
num=1
if num<=n:
    for x in range(1,n+1):
        num=num*x
    print(num)
else:
    print(num)

#or

num = int(input())
factorial = 1

while num > 0:
    factorial *= num
    num -= 1

print(factorial)
