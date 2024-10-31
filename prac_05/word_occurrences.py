"""
CP1404 Practical 5 word occurrences exercise.
Estimate: 15 minutes
Actual: 35 minutes
"""

word_to_count = {}
words = input("Text: ").split()
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
max_length = max(len(word) for word in word_to_count)

words = list(word_to_count.keys())
words.sort()
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
