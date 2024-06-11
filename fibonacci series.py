# print the series of fibonacci
def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a, end=" ")
    else:
        print(a, b, end=" ")
        for i in range(2, n):
            c = a + b
            print(c, end=" ")
            a, b = b, c
    print() 

# Example usage
n = int(input("Enter the number of terms: "))
fib(n)


# #using recursion find sum of nth fibonacci termS
# def Fibonacci(n):

# 	# Check if input is 0 then it will
# 	# print incorrect input
# 	if n < 0:
# 		print("Incorrect input")

# 	# Check if n is 0
# 	# then it will return 0
# 	elif n == 0:
# 		return 0

# 	# Check if n is 1,2
# 	# it will return 1
# 	elif n == 1 or n == 2:
# 		return 1

# 	else:
# 		return Fibonacci(n-1) + Fibonacci(n-2)

# n= int(input("Enter the nth ter for Fibonacci series: "))
# # Driver Program
# print(Fibonacci(n))
