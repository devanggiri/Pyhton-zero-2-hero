n = int(input("Enter the term upto which you want sum: "))
tsum=0
if tsum<=n:
    for x in range(1,n+1):
        tsum=tsum+x
        print(tsum, "+", x)
    print("total sum upto n terms: ", tsum)
else:
    print(tsum)

