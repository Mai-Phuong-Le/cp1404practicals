"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""

text = input("Text: ")
words = text.split()

word_to_count = {}

for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

words = sorted(word_to_count)

max_length = 0
for word in words:
    if len(word) > max_length:
        max_length = len(word)

for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")