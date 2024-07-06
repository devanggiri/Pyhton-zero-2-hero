a="Incomprehensibilities"
#  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
#-21-20-19-18-17-16-15-14-13-12-11-10-9 -8 -7 -6 -5 -4 -3 -2 -1

print(len(a))


print(a[0:11])    # selected range +ve index
print(a[-21:-10]) # selected range negative index
print(a[::])
print(a[::-1])    # all items in the array, reversed
print(a[-1:-22:-1])  # This will reverse in -ve index
print()

print(a[-11::-1]) # reversed string part with start -ve index
print(a[1::-1])   # the first two items, reversed
print(a[:-3:-1])  # the last two items, reversed
print(a[-3::-1])  # everything except the last two items, reversed