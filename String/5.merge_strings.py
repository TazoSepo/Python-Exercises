def mix_strings(str1, str2):
    if len(str1) > 2 and len(str2) > 2:
        new_str1 = str2[:2] + str1[2:]
        new_str2 = str1[:2] + str2[2:]
        result =  new_str1 + " " + new_str2
    return result

str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
print(mix_strings(str1,str2))