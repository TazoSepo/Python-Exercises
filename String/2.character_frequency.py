"""
Count character frequencies
"""
str = input("Enter the text ")
dict = {}
for i in range(len(str)):
    if str[i] in dict:
        dict[str[i]] += 1
    else:
        dict[str[i]] = 1
print(dict)