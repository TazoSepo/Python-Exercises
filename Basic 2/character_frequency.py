'''
Checking character frequencies with dictionary
'''
def read_file(filename):
    f = open("data/"+filename,"r")
    text = f.read().upper()
    return text


def count_chars(text):
    dict = {}
    for i in range(len(text)):
        if text[i] not in dict.keys():
            dict[text[i]] = 1
        else:
            dict[text[i]] += 1
    return dict

def print_dict(dict):
    for i in dict:
        print(f'Character:{i}, Frequency:{dict[i]}')

text = read_file("long_text.txt")
char_frequencies = count_chars(text)
print_dict(char_frequencies)

