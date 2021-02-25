#Count the occurrences of each word in a line of text
def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print( word_count('Pyhton is a powerful programming language and is very easy.'))