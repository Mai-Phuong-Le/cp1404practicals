"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""
from operator import itemgetter

word_to_count = {}
word_count = 0
word_length = 0

text = input("Enter text: ").split()


for word in text:
    word_count = text.count(word)
    word_to_count[word] = word_count

print(word_to_count) # dictionary chứa chữ (keys) và số chữ(word_count - values)

word_to_count = sorted(word_to_count.items(), key=itemgetter(0, 1))
# itemgetter return a pair that stored in a tuple
# câu trên return a list chứa các tuples
print(word_to_count)
word_to_count = dict(word_to_count) # convert to dict
print(word_to_count)

# cách 1 dể lấy length
# for word in word_to_count:
  #  if len(word) > word_length:
   #     word_length = len(word)
# cách 2 lấy length
word_length = (max(len(length) for length in word_to_count.keys()))

for word, count in word_to_count.items():
    print(f"{word: < {word_length}} : {count}")