import re

# Sample text
text = "Python 3.9 was released on October 5, 2020. Visit https://www.python.org for more details!"

# 1. Find all numbers
numbers = re.findall(r'\d+', text)
print("Numbers:", numbers)  # ['3', '9', '5', '2020']

# 2. Find all words
words = re.findall(r'\w+', text)
print("Words:", words)  # ['Python', '3', '9', 'was', 'released', 'on', 'October', '5', '2020', 'Visit', 'https', 'www', 'python', 'org', 'for', 'more', 'details']

# 3. Extract all URLs
urls = re.findall(r'https?://[^\s]+', text)
print("URLs:", urls)  # ['https://www.python.org']

# 4. Replace all numbers with "NUM"
cleaned_text = re.sub(r'\d+', 'NUM', text)
print("Cleaned Text:", cleaned_text)  # 'Python NUM was released on October NUM, NUM. Visit https://www.python.org for more details!'

# 5. Find specific date formats (e.g., month and year)
date = re.search(r'(\w+ \d{4})', text)
if date:
    print("Date Found:", date.group())  # 'October 2020'
