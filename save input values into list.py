# Initialize the list to store values
values = []

t = int(input("Enter the number of inputs: "))

while t > 0:
    x = int(input("Enter a value: "))
    values.insert(len(values), x)  # Insert the value of x at the end of the list
    t -= 1

# Print the list to see the stored values
print(values)



#or

# Initialize the list to store values
values = []

t = int(input())

while t > 0:
    x = int(input())
    values.append(x)  # Add the value of x to the list
    t -= 1

# Print the list to see the stored values
print(values)
print(values[1])
