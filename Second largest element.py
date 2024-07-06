# cook your dish here
for T in range(int(input())):
    a=list(map(int,input().split()))
    a.sort()
    print(a[-2])



# cook your dish here
t = int(input()) #no. of test cases
for i in range (t):
    a,b,c =list(map(int,input().split()))
    x = [a,b,c]
    x.sort(reverse=True)
    print(x[1])
    
    
