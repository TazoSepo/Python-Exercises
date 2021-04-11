def first_last2(str):
    new_str = ""
    if len(str) >= 2:
        new_str = str[0:2] + str[-2:]
    return new_str

str = input("Enter the text: ")
print(first_last2(str))