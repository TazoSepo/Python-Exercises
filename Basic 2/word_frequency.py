'''
Checking word frequency with dictionary
'''
def read_file(filename):
    words =[]
    with open("data/"+filename,'r') as f:
        for line in f:
            for word in line.split():
                words.append(word.strip('".,?!'))
    return words

def word_frequencies(words):
    dict = {}
    for i in range(len(words)):
        if words[i] not in dict.keys():
            dict[words[i]] = 1
        else:
            dict[words[i]] += 1
    return dict

def print_dict(dict):
    for i in dict:
        print(f'Word:{i}, Frequency:{dict[i]}')

words = read_file("long_text.txt")
frequencies = word_frequencies(words)

print_dict(frequencies)