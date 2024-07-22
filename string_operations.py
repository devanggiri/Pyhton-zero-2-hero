# Original string
s = " Hello, World! "

# Capitalize the first character of the string
cap_str = s.capitalize()
print("capitalize():", cap_str)

# Convert all characters to lowercase
lower_str = s.lower()
print("lower():", lower_str)

# Convert all characters to uppercase
upper_str = s.upper()
print("upper():", upper_str)

# Swap case of all characters
swapcase_str = s.swapcase()
print("swapcase():", swapcase_str)

# Title case the string
title_str = s.title()
print("title():", title_str)

# Strip leading and trailing whitespace
strip_str = s.strip()
print("strip():", strip_str)

# Strip leading whitespace
lstrip_str = s.lstrip()
print("lstrip():", lstrip_str)

# Strip trailing whitespace
rstrip_str = s.rstrip()
print("rstrip():", rstrip_str)

# Center the string with padding
center_str = s.center(20, '*')
print("center(20, '*'):", center_str)

# Left justify the string with padding
ljust_str = s.ljust(20, '*')
print("ljust(20, '*'):", ljust_str)

# Right justify the string with padding
rjust_str = s.rjust(20, '*')
print("rjust(20, '*'):", rjust_str)

# Replace a substring
replace_str = s.replace("World", "Python")
print("replace('World', 'Python'):", replace_str)

# Split the string into a list
split_str = s.split()
print("split():", split_str)

# Join a list into a string
join_str = ' '.join(split_str)
print("join(' '):", join_str)

# Find a substring
find_str = s.find("World")
print("find('World'):", find_str)

# Count occurrences of a substring
count_str = s.count("l")
print("count('l'):", count_str)

# Check if the string starts with a substring
startswith_str = s.startswith(" Hello")
print("startswith(' Hello'):", startswith_str)

# Check if the string ends with a substring
endswith_str = s.endswith("!")
print("endswith('!'):", endswith_str)

# Check if all characters in the string are alphanumeric
isalnum_str = s.isalnum()
print("isalnum():", isalnum_str)

# Check if all characters in the string are alphabetic
isalpha_str = s.isalpha()
print("isalpha():", isalpha_str)

# Check if all characters in the string are digits
isdigit_str = s.isdigit()
print("isdigit():", isdigit_str)

# Check if all characters in the string are lowercase
islower_str = s.islower()
print("islower():", islower_str)

# Check if all characters in the string are uppercase
isupper_str = s.isupper()
print("isupper():", isupper_str)

# Check if all characters in the string are whitespace
isspace_str = s.isspace()
print("isspace():", isspace_str)

# Check if the string is title cased
istitle_str = s.istitle()
print("istitle():", istitle_str)
