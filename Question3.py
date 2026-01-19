
# Second most frequent word

def findMostFrequentWord(inputList1: list[str], inputList2: list[str]) -> str:
    frequency = {}
    last_index = {}

    for i in range(len(inputList1)):
        word = inputList1[i]
        if word not in inputList2:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
            last_index[word] = i

    if len(frequency) < 2:
        return ""

    words = list(frequency.keys())

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            w1 = words[i]
            w2 = words[j]

            if (frequency[w2] > frequency[w1]) or \
               (frequency[w2] == frequency[w1] and last_index[w2] > last_index[w1]):
                words[i], words[j] = words[j], words[i]

    return words[1]



# Most frequent word in text

def findMostFrequentWordInText(text: str) -> str:
    excluded_words = ["a", "the", "in", "of", "and", "to", "be", "is"]

    text = text.lower()

    punctuation = ".,!?;:\"()[]{}"
    for char in punctuation:
        text = text.replace(char, "")

    words = text.split()

    frequency = {}
    last_index = {}

    for i in range(len(words)):
        word = words[i]
        if word not in excluded_words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
            last_index[word] = i

    if len(frequency) == 0:
        return ""

    unique_words = list(frequency.keys())

    for i in range(len(unique_words)):
        for j in range(i + 1, len(unique_words)):
            w1 = unique_words[i]
            w2 = unique_words[j]

            if (frequency[w2] > frequency[w1]) or \
               (frequency[w2] == frequency[w1] and last_index[w2] > last_index[w1]):
                unique_words[i], unique_words[j] = unique_words[j], unique_words[i]

    return unique_words[0]


# Test for part (a)
a1 = ["dog", "cat", "dog", "bird", "cat", "dog", "cat"]
a2 = ["bird"]

print(findMostFrequentWord(a1, a2))



# Test for part (b)
text = "Life is beautiful and life is full of surprises. Life brings joy and life brings hope."
print(findMostFrequentWordInText(text))

